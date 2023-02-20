compressed_file_name = 'img/logo.jpg'


fileR = open(compressed_file_name, "rb")
payloader = bytearray()
chunk = 0
i=2
byte = fileR.read(28)
while byte:
    i+=1
    if (i%200) !=0:
        payloader+=(byte)
    else:
        print('no')
    # Read next 28 bytes
    byte = fileR.read(28)
    # chunk += 1

 
fileT = open('picture/final_data.bin', "wb")
fileT.write(payloader)
fileT.close()