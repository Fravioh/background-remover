from rembg import remove 
from PIL import Image

imageJPG_path = 'Teemo_TurnTable_img.jpg'
imagePNG_path = 'Teemo_TurnTable_img.PNG'

inp = Image.open(imageJPG_path)

imageJPG = remove(inp)
imageJPG.save(imagePNG_path)