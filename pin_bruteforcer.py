# Bruteforce eines 1 bis 4-stelligen Pins
import time


def pin_bruteforcer(n):
    ergebnis = 0
    counter = 0
    while ergebnis != str(n):
        start = time.time()
        for a in range(0, 10):
            counter += 1
            for b in range(0, 10):
                counter += 1
                for c in range(0, 10):
                    counter += 1
                    for d in range(0, 10):
                        counter += 1
                        if f'{a}{b}{c}{d}' == str(n):
                            end = time.time()
                            print(f'Versuchsanzahl = {counter}\nIn : {(end - start) * 1000} Millisekunden')
                            ergebnis = f'{a}{b}{c}{d}'


pin_bruteforcer(9596)
