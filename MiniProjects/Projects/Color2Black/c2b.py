from PIL import Image
fileLocation = raw_input("Enter The Location Of The File : ")
openImage = Image.open(fileLocation)
convertTobw = openImage.convert("L")
convertTobw.show()
