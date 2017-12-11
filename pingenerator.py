#!/usr/bin/env python

import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("number_of_pins", type=int,
                    help="number of pin numbers to generate")
args = parser.parse_args()

secure_random = random.SystemRandom()

pin_list = []

for i in range(args.number_of_pins):
    # print secure_random.choice(usable_words)+secure_random.choice(usable_words)
    pin = ''.join(secure_random.sample("0123456789", 5))
    while pin in pin_list:
        pin = ''.join(secure_random.sample("0123456789", 5))
    pin_list.append(pin)

for pin in pin_list:
    print(pin)
