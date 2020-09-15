def countBits(n):
    binary = bin(n)
    return binary[2:].count('1')