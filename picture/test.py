from PIL import Image

image = Image.open('picture/qwe.jpg')
data = list(image.getdata())
image2 = Image.new(image.mode, image.size)
image2.putdata(data)
image2.save('picture/qwe1.jpg')