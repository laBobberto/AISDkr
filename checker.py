import random
from decimal import Decimal, getcontext
import math
import time

from tqdm import tqdm

import chudnovsky_pi
import leibniz_pi

getcontext().prec = 1000
ideal_pi = "3.141592653589793238462643383279"
ideal_pi_len = 32


def find_pi_to_ten_digits(func, step=100):
    results = []
    n = 1
    correct_digits = 0

    for n in tqdm(range(1, 100_000_000, step)):
        timer = time.time()
        calculated_pi = str(func(n))
        timer = time.time() - timer


        if correct_digits == ideal_pi_len:
            return results
        if calculated_pi[correct_digits] == ideal_pi[correct_digits]:
            correct_digits += 1
            print(correct_digits, calculated_pi, timer)
            results.append([correct_digits, timer])
    if correct_digits != ideal_pi_len:
        for n in range(1, 100_000_000, step):
            timer = time.time()
            calculated_pi = str(func(n))
            timer = time.time() - timer


            if correct_digits == ideal_pi_len:
                return results
            if calculated_pi[correct_digits] == ideal_pi[correct_digits]:
                correct_digits += 1
                print(correct_digits, calculated_pi, timer)
                results.append([correct_digits, timer])


def create_data_file(data, filename):
    filename = filename.__qualname__ + ".txt"
    with open(filename, encoding="UTF-8", mode="w+") as file:
        data = str(data).replace("], ", "\n").replace("[", "").replace(",", "").replace("]]", "")
        file.write(data)

print()
create_data_file(find_pi_to_ten_digits(chudnovsky_pi.chudnovsky_pi, 100), chudnovsky_pi.chudnovsky_pi)
# print(wallis_pi(5**5))


