from OpenGL.GL import *
from PIL import Image
import numpy as np

def load_texture(filename, texture_id):
    # Load the image file using PIL
    image = Image.open(filename)
    img_data = np.array(list(image.getdata()), np.uint8)
    width, height = image.size

    # Bind the texture
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Set the texture wrapping parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    # Set texture filtering parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # Generate and load the texture
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    glGenerateMipmap(GL_TEXTURE_2D)

    # Return the texture ID
    return texture_id
