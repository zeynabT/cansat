from PIL import Image
import time
import struct

compressed_file_name = 'img/logo.jpg'


# with open(compressed_file_name,'rb') as im:
#     pic_data=im.read()
# payloader = bytearray()
# payloading = 27

# for item in range(int(len(pic_data)/payloading)+1):
#     bufferi = b''.join( [bytearray(('-_-'+str(item)+'-').encode()), pic_data[(item*payloading) : (item+1)*payloading]])
#     payloader += bufferi

# with open("picture/final_data.bin", "wb") as f:
#         f.write(payloader)
#         f.close()

# File to open and break apart
fileR = open(compressed_file_name, "rb")
payloader = bytearray()
chunk = 0

byte = fileR.read(28)
while byte:
    # Open a temporary file and write a chunk of bytes
    name =  str(chunk)
    name=name.encode()
    payloader+=(name+byte)
    # Read next 28 bytes
    byte = fileR.read(28)
    chunk += 1

 
fileT = open('picture/final_data.bin', "wb")
fileT.write(payloader)
fileT.close()
     


