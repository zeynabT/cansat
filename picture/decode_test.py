





file = open('picture/final_data.bin', 'rb')
output = file.read()


payloader = bytearray()
for i in range(int(len(output)/28)+1):
    s2 = output[:28]
    output = output[28:]
    payloader+=s2

fileT = open('picture/decode.jpg', "wb")
fileT.write(payloader)
fileT.close()
