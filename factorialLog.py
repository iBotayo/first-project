import logging

logging.basicConfig(filename='factorial.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('start of factorial (n=%s)', n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s', i, total)
    logging.debug('End of factorial (n=%s)', n)
    return total

print(factorial(8))
logging.debug('End of program')