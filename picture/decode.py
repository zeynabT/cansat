file=open('picture/final_data.bin','rb')
output=''
output=((file.read()))
print()

payloader = bytearray()

for i in range(int(len(output)/28)+1):
    
    s1=output[:len(str(i))]
    output=output[len(str(i)):]
    s2=output[:28]
    output=output[28:]
    payloader+=s2
    print(s1)
    print(s2)

fileT = open('picture/decode.jpg', "wb")
fileT.write(payloader)
fileT.close()





# print(output[3].find('-'))
# print(output[3][output[3].find('-')+1:])

# # for i in range(50):
# #     output=output+((file.readline()))
# # outpust.
# Open original file for reconstruction
# fileM = open("picture/final_data.bin", "wb"
# # Manually enter total amount of "chunks"
# chunk = 0
# chunks = 100
# # Piece the file together using all chunks
# while chunk <= chunks:
#     print(" - Chunk #" + str(chunk) + " done.")
#     fileName = "chunk" + str(chunk) + ".txt"
#     fileTemp = open(fileName, "rb")
#     byte = fileTemp.read(1024)
#     fileM.write(byte)
#     chunk += 1
# fileM.close()