from PIL import Image
import time
import struct

pic_list =[]

compressed_file_name = 'ww.jpg'


with open(compressed_file_name,'rb') as im:
    pic_data=im.read()
payloader = bytearray()
payloading = 26

for item in range(int(len(pic_data)/payloading)+1):
    # "<f" means a single little endian (4 byte) float value.
    # bufferi = bytes()
    bufferi = b''.join( [bytearray((str(100000+item)).encode()), pic_data[(item*payloading) : (item+1)*payloading]])
    payloader += bufferi

print(payloader)


# print(payloader)

# print(payloader)

with open("final_data2.bin", "wb") as f:
        f.write(payloader)
        f.close()