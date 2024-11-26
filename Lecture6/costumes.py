import sys 

from PIL import Image  

images = [] 
for item in sys.argv[1:]: 
    image = Image.open(item) 
    images.append(image) 

images[0].save(
    "costumes.gif", append_images=[images[1]], save_all=True, duration=200, loop=0
)