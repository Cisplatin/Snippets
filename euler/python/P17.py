"""
Number Letter Counts
Problem 17
"""

words = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
}

if __name__ == '__main__':
    # This is a pretty dirty solution. We basically go through each number
    # from 1 to 1000 looking for certain characteristics.
    result = len('onethousand')
    for i in range(1, 1000):
        # Take care of the hundred's place
        if i >= 100:
            result += len(words[i / 100]) + len('hundred')
            if not i % 100:
                result += len('and')
            i %= 100
        # Then the ten's place (unless it's below 20)
        if i >= 20:
            result += len(words[(i / 10) * 10])
            i %= 10
        # Then the final digit
        result += len(words[i])
    print result
