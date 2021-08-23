"""
Take input as number
Output hex codes up to number of requested colors
"""
from random import *
import pyperclip
import math

def print_hex(n=3):
        collection = []
        for i in range(n):
                collection.append(make_hex_code())
        print('hex codes made.')
        print('{} colors copied to clipboard!'.format(len(collection)))
        collection = ',\n'.join(collection).lower()
        pyperclip.copy(collection)
        print(collection)

def make_hex_code():
        digits = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']

        if prefix_position == 1:
                hex_code = '#{}{}{}{}{}'.format(hex_prefix, choice(digits), choice(digits), choice(digits), choice(digits))
        elif prefix_position == 2:
                hex_code = '#{}{}{}{}{}'.format(choice(digits), choice(digits),hex_prefix, choice(digits), choice(digits))
        elif prefix_position == 3:
                hex_code = '#{}{}{}{}{}'.format(choice(digits), choice(digits), choice(digits), choice(digits),hex_prefix)
        return hex_code

if __name__ == '__main__':
        i = 0
        while True:
                i += 1
                try:
                        print('select a prefix position: (1)front (2)middle (3)end')
                        prefix_position = int(input('> '))
                        if prefix_position != 1 or prefix_position != 2 or prefix_position != 3:
                                print('invalid prefix position. use (1), (2), or (3).')
                                prefix_position = int(input('> '))
                        print()

                        hex_prefix = str(input('enter a 2-character hex prefix (example: a3): '))

                        if len(hex_prefix) != 2:
                                print('incorrect length. use 2 characters.')
                                hex_prefix = str(input('enter a 2-character hex prefix (example: a3): '))

                        n = abs(int(input('how many colors will be in your palette? ')))

                except ValueError:
                        n = abs(int(input('please enter a valid integer: ')))

                print_hex(n)
                print()

                if i > 5:
                        print('ending program')
                        break
