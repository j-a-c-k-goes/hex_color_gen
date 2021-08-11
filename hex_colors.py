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
        collection = '\n'.join(collection).upper()
        pyperclip.copy(collection)
        print(collection)
def make_hex_code():
        digits = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
        hex_code = '#{}{}{}{}{}{}'.format(choice(digits), choice(digits), choice(digits), choice(digits), choice(digits), choice(digits))
        return hex_code
if __name__ == '__main__':
        try:
                n = abs(int(input('how many colors will be in your palette? ')))
        except ValueError:
                n = abs(int(input('please enter a valid integer: ')))
        print_hex(n)
"""
Future updates: detect color for given generated hex code, if #000000, black
"""
