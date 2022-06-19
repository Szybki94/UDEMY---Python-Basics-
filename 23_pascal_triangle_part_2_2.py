numbers = [1]
triangle_width = 50
triangle_height = 7

def line_create():
    
    line = ''
    for n in numbers:
        line += "%3d" % n
    print(line.center(triangle_width))

line_create()

for i in range(triangle_height - 1):

    new_numbers = [1]

    position = 0
    while position < len(numbers) - 1:
        new_numbers.append(numbers[position] + numbers[position+1])
        position += 1

    new_numbers.append(1)
    numbers = new_numbers.copy()

    line_create()
