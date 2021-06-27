segments = {
    '0': (' __ ', '|  |', '|__|'),
    '1': ('    ', '   |', '   |'),
    '2': (' __ ', ' __|', '|__ '),
    '3': (' __ ', ' __|', ' __|'),
    '4': ('    ', '|__|', '   |'),
    '5': (' __ ', '|__ ', ' __|'),
    '6': (' __ ', '|__ ', '|__|'),
    '7': (' __ ', '   |', '   |'),
    '8': (' __ ', '|__|', '|__|'),
    '9': (' __ ', '|__|', ' __|'),
    ':': (' ', '•', '•'),
    '_': ('    ', '    ', ' __ ')
}

input = input('Input: ')

if (len(input) != 8 or input[2] != ':' or input[5] != ':' or int(input[3]) > 5 or int(input[6]) > 5):
    input = '__:__:__'
# print 3 lines, line 1, 2, 3 containing the top, middle, and bottom part of the numbers
for i in range(3):
        print(' '.join(segments[str(number)][i] for number in input))