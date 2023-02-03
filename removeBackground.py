from rembg import remove
from PIL import Image

input_file = 'image.jpeg'
output_file = 'output.jpeg'
inputImg = Image.open(input_file)
rgb_im = inputImg.convert('RGB')
outputImg = remove(rgb_im)
outputImg.save(output_file)
