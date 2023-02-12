

file = open('picture/final_data2.bin', 'rb')
output = ''
output = file.read()

black_img = 'picture/black.jpg'
black_file = open(black_img, "rb")
black_file = black_file.read()


payloader = bytearray()
sum = 0
for i in range(int(len(output)/32)+1):
    s1 = output[:6]
    s1 = int(s1.decode())-100000
    output = output[6:]
    s2 = output[:26]
    output = output[26:]
    if (500< s1 and s1<1000):
        sum += 1
        # payloader += black_file[(s1*26):((s1+1)*26)+1]
        payloader += s2
    print(s1)


# from PIL import Image
# from io import BytesIO

# im = Image.open(BytesIO(payloader))

# # Display image
# im.show()
# print(im)
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
