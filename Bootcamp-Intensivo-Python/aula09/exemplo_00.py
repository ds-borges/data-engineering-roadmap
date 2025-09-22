import time

from timer import time_measure_decorator

# from loguru import logger
# from sys import stderr

# Configuração do logger para stderr
# logger.add(
#                sink=stderr,
#                format="{time} <r>{level}</r> <g>{message}</g> {file}",
#                level="INFO"
#          )


@time_measure_decorator
def soma(x, y):
    soma = x + y
    time.sleep(2)
    print(f"Voce digitou valores em formato corretor, parabens {soma}")
    return soma


soma(2, 7)
soma(2, 5)
