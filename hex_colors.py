"""
Take input as number
Output hex codes up to number of requested colors
"""

# ............................................................ Imports
from random import *
import pyperclip
# ............................................................ Function
def make_hex_code(number_of_colors = 3):

	hex_codes = []

	digits = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']

	for i in range(number_of_colors):
		hex_code = '#%s%s%s%s%s%s' % (choice(digits), choice(digits), choice(digits), choice(digits), choice(digits), choice(digits))
		hex_codes.append(hex_code)

	pyperclip.copy('\n'.join(hex_codes).upper())

	print('%s colors copied to clipboard!'  % (number_of_colors))

	print('\n'.join(hex_codes).upper())

	"\n".join(hex_codes)

	return hex_codes
# ............................................................ On Run
if __name__ == '__main__':

        number_of_colors = int(input('how many colors will be in your palette? '))

        make_hex_code(number_of_colors)

"""
Future updates: detect color for given generated hex code, if #000000, black
"""
