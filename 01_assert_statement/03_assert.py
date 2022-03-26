width = int(input('Enter the width of the rectangle: '))
height = int(input('Enter the height of the rectangle: '))

assert width > 0, 'The width value must be possitive.'
assert height > 0, 'The height value must be possitive.'

area = width * height
print(f'Area: {area:.2f}')