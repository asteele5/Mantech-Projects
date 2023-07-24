#-i = encrypted file path
#-o name of output file
#-k = key for xor cipher

import sys
import getopt

key = None
input = None
output = None

try:
    opts, args = getopt.getopt(sys.argv[1:],"i:o:k:")
except:
    print("Argument error")
    exit()

for opt, arg in opts:
    if opt in ['-i']:
        input = arg
    elif opt in ['-k']:
        key = arg
    elif opt in ['-o']:
        output = arg

input_file = bytearray(open(input,'rb').read())
byte_key = bytearray(key, 'utf-8')
byte_output = bytearray(len(input_file))
j = 0

for i in range(len(input_file)):
    if(j == len(key)):
        j = 0
    byte_output[i] = input_file[i] ^ byte_key[j]
    j += 1

output_file = open(output, 'wb')
output_file.write(byte_output)
output_file.close()







