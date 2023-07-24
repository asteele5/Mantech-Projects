
def rotate_bits_left(num, amount):
    #ex: num = 10101111 amount = 4
    # print('original: '+bin(num))
    #101011110000 OR 1010 = 101011111010
    num = (num << amount) | (num >> 8-amount)
    #101011111010 AND ~(111100000000) = 101011111010 AND 000011111111 = 11111010
    num = num & ~(2**amount-1 << 8)
    # print('shifted: '+bin(num))
    return num

def rotate_bits_right(num, amount):
    print('this function isn\'t ready yet')

bytes = bytearray(open('level2_data', 'rb').read())

for i in range(len(bytes)):
    bytes[i] = rotate_bits_left(bytes[i], 4)

decrypted = bytes.decode('latin-1')
print(decrypted)


