# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
from configuration import go_configure, load_jwt, save_jwt
from blue_yonder import Butterfly
import yaml

plain_text = """    This is an example of a plain text post.
A plain text post is a post that contains only text and no images. It is a simple way to post text to BlueSky. The maximum length of a plain text post is 290 characters. 
    Two hundred and ninety characters are pretty much enough if you . . .
"""

POST_FILE = './data/post_data.yaml'


if __name__ == "__main__":
    """
    This is an example of a plain text post.
    """
    print(len(plain_text))  # let's check the length

    # if you don't want to set the environment variables
    # just store the credentials in the configuration file.
    # See the config_example.yaml

    config = go_configure(config_file='config_example.yaml')

    butterfly = Butterfly(
        bluesky_handle  =getenv('BLUESKY_HANDLE', config['BLUESKY_HANDLE']),
        bluesky_password=getenv('BLUESKY_PASSWORD', config['BLUESKY_PASSWORD']),
        jwt=load_jwt()
    )
    save_jwt(butterfly.publish_jwt())

    # Now, post the text
    result = butterfly.post(plain_text)

    # We will store the post data in a yaml file
    with open(POST_FILE, 'w') as post_file:
        yaml.dump(result, post_file)

    with open(POST_FILE, 'r') as post_file:
        post_data = yaml.load(post_file, Loader=yaml.FullLoader)

    ...
