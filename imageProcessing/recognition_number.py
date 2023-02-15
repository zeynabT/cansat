from number_recognition import NumberRecognizer

n = NumberRecognizer()

n.init() # create a model
n.load() # load the model

num = n.recognize('path/to/image_28x28.png') # recognise the image
print(f"the number is {num}")