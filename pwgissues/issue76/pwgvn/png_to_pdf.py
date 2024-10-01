from PIL import Image
import sys
def convert(filein,fileout):
 # Open the PNG image
 image = Image.open(filein)
 # Convert the image to RGB (necessary for PDF conversion)
 image = image.convert('RGB')
 # Save the image as a PDF
 image.save(fileout)
 
if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 convert(filein,fileout)

