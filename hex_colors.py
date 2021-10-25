from random import *
import pyperclip
def color_base():
        colors_base = ['red', 'green', 'blue']
        return colors_base
def select_color():
        select_color = str(input('for color generation, enter "red", "green", or "blue": '))
        return select_color
selected_color = select_color()
while selected_color not in color_base():
        print('use red green or blue to generate colors')
        selected_color = select_color()
def hex_digits():
         digits = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
         return choice(digits)
def make_hex_code():
        max_hex_value = 'ff'
        if selected_color == 'red': hex_code = f'{max_hex_value}{hex_digits()}{hex_digits()}{hex_digits()}{hex_digits()}'
        elif selected_color == 'green': hex_code = hex_code = f'{hex_digits()}{hex_digits()}{max_hex_value}{hex_digits()}{hex_digits()}'
        elif selected_color == 'blue': hex_code = hex_code = f'{hex_digits()}{hex_digits()}{hex_digits()}{hex_digits()}{max_hex_value}'
        return hex_code
def print_hex_values():
        palette = []
        if selected_color == "red": print('generating red dominant values')
        elif selected_color == "green": print('generating green dominant values')
        elif selected_color == "blue": print('generating blue dominant values')
        for color in range(number_of_colors):
                palette.append(make_hex_code())
        for index, color in enumerate(palette):
                print(f'{index}\t{color}')
        palette = '\n'.join(palette).upper()
        pyperclip.copy(palette)
        print(f'colors copied to clipboard!')
        return palette
if __name__ == '__main__':
        number_of_colors = int(input('enter how many color options to generate: '))
        print_hex_values()
