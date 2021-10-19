from random import *
import pyperclip
import math
colors_base = ['red', 'green', 'blue']
select_color = str(input('for color genration, enter "red", "green", or "blue": '))
while select_color not in colors_base:
        print('use red green or blue to generate colors')
        select_color = str(input('for color generation, enter "red", "green", or "blue": '))
number_of_colors = int(input('enter how many color options to generate: '))
max_hex_value = 'ff'
def hex_digits():
         digits = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
         return choice(digits)
def make_hex_code():
        if select_color == 'red':
                hex_code = f'{max_hex_value}{hex_digits()}{hex_digits()}{hex_digits()}{hex_digits()}'
        elif select_color == 'green':
                hex_code = hex_code = f'{hex_digits()}{hex_digits()}{max_hex_value}{hex_digits()}{hex_digits()}'
        elif select_color == 'blue':
                hex_code = hex_code = f'{hex_digits()}{hex_digits()}{hex_digits()}{hex_digits()}{max_hex_value}'
        return hex_code
def print_hex_values():
        palette = []
        if select_color == "red":
                print('generating red dominant colors')
        elif select_color == "green":
                print('generating green dominant colors')
        elif select_color == "blue":
                print('generating blue dominant colors')
        for color in range(number_of_colors):
                palette.append(make_hex_code())
        print('hex codes made.')
        print(f'{len(palette)} colors copied to clipboard!')
        palette = '\n'.join(palette).upper()
        pyperclip.copy(palette)
        print(palette)
print_hex_values()
