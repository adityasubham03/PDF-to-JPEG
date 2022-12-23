from wand.image import Image as wi
file = input("Enter the name of the file:- ")
PDFfile = wi(filename=file,resolution=400)
Images = PDFfile.convert('jpg')
ImageSequence = 1

for img in PDFfile.sequence:
    Image = wi(image = img)
    Image.save(filename="Image"+str(ImageSequence)+".jpg")
    ImageSequence += 1
