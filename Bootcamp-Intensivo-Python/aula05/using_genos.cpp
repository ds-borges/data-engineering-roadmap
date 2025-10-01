/**
 * @file using_genos.cpp
 * @brief Processador de alto desempenho para o "Desafio de 1 Bilhão de Linhas" em C++.
 *
 * Este programa calcula as temperaturas mínima, média e máxima para estações
 * meteorológicas a partir de um arquivo de texto de grande volume. Ele foi
 * otimizado para máxima performance utilizando as seguintes técnicas:
 *
 * 1. Mapeamento de Memória (mmap): O arquivo inteiro é mapeado diretamente na
 * memória virtual, evitando a sobrecarga de chamadas de leitura do disco.
 * 2. Multithreading: O trabalho é dividido entre todos os núcleos de CPU
 * disponíveis para processamento paralelo.
 * 3. Agregação Local: Cada thread tem seu próprio mapa de resultados para
 * eliminar a necessidade de bloqueios (mutexes) e evitar contenção.
 * 4. Parser Otimizado: Uma função customizada (`fast_stod`) e ultrarrápida
 * é usada para converter as temperaturas de texto para número.
 *
 * @author Diego S. Borges
 * @version 1.2
 * @date 2025-09-10
 *
 * @compilation Para compilar este arquivo, use um comando como:
 * g++ -std=c++17 -O3 -o using_genos using_genos.cpp -lpthread
 */

// --- Bibliotecas Padrão ---
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <thread>
#include <unordered_map>
#include <algorithm>
#include <iomanip>
#include <chrono>

// --- Bibliotecas de Sistema (para mmap) ---
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

/**
 * @struct Measurement
 * @brief Armazena os dados agregados para uma única estação meteorológica.
 */
struct Measurement {
    double min_temp = 100.0;
    double max_temp = -100.0;
    double sum_temp = 0.0;
    long long count = 0;

    /**
     * @brief Atualiza as estatísticas com uma nova medição de temperatura.
     * @param temp A nova temperatura a ser processada.
     */
    void update(double temp) {
        if (temp < min_temp) min_temp = temp;
        if (temp > max_temp) max_temp = temp;
        sum_temp += temp;
        count++;
    }
};

/**
 * @brief Mescla um mapa de resultados de uma thread no mapa de resultados principal.
 */
void merge_maps(std::unordered_map<std::string, Measurement>& main_map, const std::unordered_map<std::string, Measurement>& thread_map) {
    for (const auto& pair : thread_map) {
        Measurement& main_measure = main_map[pair.first]; // Acessa ou cria a estação no mapa principal
        main_measure.min_temp = std::min(main_measure.min_temp, pair.second.min_temp);
        main_measure.max_temp = std::max(main_measure.max_temp, pair.second.max_temp);
        main_measure.sum_temp += pair.second.sum_temp;
        main_measure.count += pair.second.count;
    }
}

/**
 * @brief Converte uma string de caracteres para double de forma otimizada.
 */
double fast_stod(const char* p) {
    bool is_neg = *p == '-';
    if (is_neg) ++p;

    int val = 0;
    if (p[1] == '.') { // Formato X.X
        val = (p[0] - '0') * 10 + (p[2] - '0');
    } else { // Formato XX.X
        val = (p[0] - '0') * 100 + (p[1] - '0') * 10 + (p[3] - '0');
    }

    return is_neg ? -val / 10.0 : val / 10.0;
}

/**
 * @brief Função executada por cada thread para processar uma fatia do arquivo.
 */
void process_chunk(const char* start, const char* end, std::unordered_map<std::string, Measurement>& results) {
    const char* current = start;

    // Tratamento de borda: avança para o início da próxima linha se o chunk começar no meio de uma.
    if (start != 0 && *(start - 1) != '\n') {
        while (current < end && *current != '\n') {
            current++;
        }
        current++;
    }

    while (current < end) {
        const char* line_start = current;
        const char* semicolon = nullptr;

        // Loop para encontrar o fim da linha e o ';' sem criar novas strings.
        while (current < end && *current != '\n') {
            if (*current == ';') {
                semicolon = current;
            }
            current++;
        }

        if (semicolon) {
            std::string station(line_start, semicolon - line_start);
            double temp = fast_stod(semicolon + 1);

            results[station].update(temp); // Atualiza o mapa de resultados LOCAL da thread.
        }

        if (current < end) current++; // Pula o caractere '\n'
    }
}

/**
 * @brief Ponto de entrada principal do programa.
 */
int main() {
    const std::string filename = "One-Billion-Row-Challenge-Python/data/measurements.txt";
    auto start_time = std::chrono::high_resolution_clock::now(); // Inicia o cronômetro de alta precisão

    // --- ETAPA 1: Mapear o arquivo na memória (mmap) ---
    int fd = open(filename.c_str(), O_RDONLY); // Abre o arquivo em modo de apenas leitura
    if (fd == -1) {
        std::cerr << "Erro ao abrir o arquivo." << std::endl; return 1;
    }

    struct stat sb;
    if (fstat(fd, &sb) == -1) { // Pega as estatísticas do arquivo, incluindo o tamanho
        close(fd); std::cerr << "Erro ao obter o tamanho do arquivo." << std::endl; return 1;
    }
    long long file_size = sb.st_size;

    // Mapeia o arquivo na memória para acesso ultrarrápido, evitando leituras de disco
    const char* mapped_file = static_cast<const char*>(mmap(NULL, file_size, PROT_READ, MAP_PRIVATE, fd, 0));
    if (mapped_file == MAP_FAILED) {
        close(fd); std::cerr << "Erro ao mapear o arquivo na memória." << std::endl; return 1;
    }

    // --- ETAPA 2: Dividir o trabalho e iniciar as threads ---
    unsigned int num_threads = std::thread::hardware_concurrency(); // Pega o número de núcleos de CPU disponíveis
    std::vector<std::thread> threads;
    std::vector<std::unordered_map<std::string, Measurement>> thread_results(num_threads); // Um mapa de resultados para cada thread
    long long chunk_size = file_size / num_threads;

    // Lança uma thread para cada "fatia" do arquivo
    for (unsigned int i = 0; i < num_threads; ++i) {
        const char* chunk_start = mapped_file + i * chunk_size;
        const char* chunk_end = (i == num_threads - 1) ? (mapped_file + file_size) : (mapped_file + (i + 1) * chunk_size);
        threads.emplace_back(process_chunk, chunk_start, chunk_end, std::ref(thread_results[i]));
    }

    // --- ETAPA 3: Esperar e juntar os resultados ---
    for (auto& t : threads) {
        t.join(); // Bloqueia a thread principal até que a thread 't' termine seu trabalho.
    }

    munmap((void*)mapped_file, file_size); // Libera a memória mapeada
    close(fd); // Fecha o descritor do arquivo

    // Junta os resultados de todas as threads em um único mapa final
    std::unordered_map<std::string, Measurement> final_results;
    for (const auto& res : thread_results) {
        merge_maps(final_results, res);
    }

    // --- ETAPA 4: Ordenar e imprimir ---
    std::vector<std::string> sorted_stations;
    sorted_stations.reserve(final_results.size()); // Pre-aloca memória para evitar realocações
    for (const auto& pair : final_results) {
        sorted_stations.push_back(pair.first);
    }
    std::sort(sorted_stations.begin(), sorted_stations.end()); // Ordena os nomes das estações alfabeticamente

    std::cout << std::fixed << std::setprecision(1); // Configura a saída para ter uma casa decimal
    for (const auto& station : sorted_stations) {
        const auto& m = final_results[station];
        std::cout << station << "=" << m.min_temp << "/" << (m.sum_temp / m.count) << "/" << m.max_temp << std::endl;
    }

    auto end_time = std::chrono::high_resolution_clock::now(); // Para o cronômetro
    std::chrono::duration<double> elapsed = end_time - start_time;

    // Imprime o tempo de execução no erro padrão para não poluir a saída principal
    std::cerr << "Genos Took: " << std::fixed << std::setprecision(2) << elapsed.count() << " sec" << std::endl;

    return 0; // Sucesso
}
