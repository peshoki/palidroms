'''
Cehck if given number is palidromic on given base.
'''
def checkPalindrom(decimal, base):
    if base < 2:
        return False
    palidromArray = []
    while decimal:
        palidromArray.append(int(decimal % base))
        decimal /= base
    return  palidromArray == palidromArray[::-1]

'''
Stores result of checking for poligromic numbers in range.
'''
def processPalidromCheck(minDecimal, maxDecimal):
    result = []
    for currentDecimal in range(minDecimal, maxDecimal):
        currentBase = 2
        while not checkPalindrom(currentDecimal, currentBase):
            currentBase += 1
        result.append([currentDecimal, currentBase])
    return result
