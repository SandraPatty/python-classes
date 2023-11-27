
import os
import numpy as np
from PIL import Image


for i in range(1, 4):
    image = np.array(Image.open(os.path.join('lunar_images', f'lunar0{i}_raw.jpg')))

    minimum = image.min()
    maximum = image.max()

    image = (255 / (maximum - minimum) * (image - minimum)).astype(np.uint8)
    
    image = Image.fromarray(image)
    image.save(f'lunar0{i}_cooked.jpg')

