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

external_link_post_text = """This is a template repository with examples of `blue_yonder` package usage. Click the "Use this template" button at the top of this page and create a copy of this repo in your account where you will be able to use and modify it the way you want."""
THUMBNAIL_FILE = './images/butterfly_big.jpg'
MIME_TYPE = 'image/jpeg'
image_alt_text = 'This is an image of a butterfly.'
title = 'Butterfly'
description = """Butterfly is a template repository with examples of how to use `blue_yonder`
package. It is a collection of Python scripts for the Bluesky social network. """
url = 'https://github.com/alxfed/butterfly'


def main():
    """ This is an example of posting an image.
    """
    butterfly = Butterfly(jwt=load_jwt())
    save_jwt(butterfly.jwt)

    # You don't need to detect image sizehere.

    # Upload the image, get a blob data
    uploaded_blob = butterfly.upload_image(file_path=THUMBNAIL_FILE, mime_type=MIME_TYPE)

    # Post a post with an embedded image
    post_with_external_link = butterfly.post_external(
        url=url,                        # required, url of the external page;
        text=external_link_post_text,   # required, pass an empty string '' if not needed;
        title=title,                    # required, non-empty string;
        description=description,        # required, non-empty string;
        thumb=uploaded_blob             # optional, don't pass this parameter if not needed.
    )
    return post_with_external_link


if __name__ == "__main__":
    post = main()
...