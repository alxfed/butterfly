# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from configuration import load_jwt, save_jwt
from blue_yonder import Butterfly
from PIL import Image
import os


image_post_text = 'This is a post with an embedded image. As it turns out the text accompanying your image can be quite long but if you don\'t need it, you can simply pass an empty string.'
IMAGE_FILE = './images/butterfly_big.jpg'
# MIME_TYPE = 'image/jpeg'
# IMAGE_FILE = './images/butterfly.png'
# MIME_TYPE = 'image/png'
image_alt_text = 'This is an image of a butterfly.'


def main():
    """ This is an example of posting an image.
    """
    butterfly = Butterfly(jwt=load_jwt())
    save_jwt(butterfly.jwt)

    # Detect image dimensions and type
    with Image.open(IMAGE_FILE) as img:
        width, height = img.size
        format = img.format.lower()

    aspect_ratio = {
        'height': height,
        'width': width
    }
    MIME_TYPE = f'image/{format}'

    # Check if image file size is too big
    file_size = os.path.getsize(IMAGE_FILE)
    if file_size > 1000000:
        print('Image size is too big.')
        return

    # Upload the image, get a blob data
    uploaded_blob = butterfly.upload_image(file_path=IMAGE_FILE, mime_type=MIME_TYPE)

    # Post a post with an embedded image
    post_with_image = butterfly.post_image(text=image_post_text, blob=uploaded_blob, alt_text=image_alt_text, aspect_ratio=aspect_ratio)


if __name__ == "__main__":
    main()
...
