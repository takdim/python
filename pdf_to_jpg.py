# import module
from pdf2image import convert_from_path
 
 

images = convert_from_path('sample.pdf')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
