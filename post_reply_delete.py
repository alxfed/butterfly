# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
from configuration import load_jwt, save_jwt
from blue_yonder import Butterfly
import yaml

plain_text = """    This is an example of a plain text post.
A plain text post is a post that contains only text and no images. 
"""
plain_text_reply = """    This is an example of a plain text reply to a post.
"""

POST_FILE = './data/post_data.yaml'
REPLY_FILE = './data/reply_data.yaml'


if __name__ == "__main__":
    """
    This is an example of a plain text post.
    """
    print(len(plain_text))  # let's check the length

    butterfly = Butterfly(
        bluesky_handle  =getenv('BLUESKY_HANDLE'),
        bluesky_password=getenv('BLUESKY_PASSWORD'),
        jwt=load_jwt()
    )
    save_jwt(butterfly.publish_jwt())

    # Now, post the text
    result = butterfly.post(plain_text)

    # We will store the post data in a yaml file
    with open(POST_FILE, 'w') as post_file:
        yaml.dump(result, post_file)

    # Read the post data
    with open(POST_FILE, 'r') as post_file:
        post_data = yaml.load(post_file, Loader=yaml.FullLoader)

    # Now, post the reply
    result = butterfly.reply(root_post=post_data, post=post_data, text=plain_text_reply)

    # We will store the reply data in a yaml file too.
    with open(REPLY_FILE, 'w') as reply_file:
        yaml.dump(result, reply_file)

    """ Look at your bluesky profile and you will see the post and reply.
        Now we can delete the reply and the post.
    """

    # Read the data of the reply that you want to delete
    with open(REPLY_FILE, 'r') as reply_file:
        reply_data = yaml.load(reply_file, Loader=yaml.FullLoader)

    # Now, delete the reply
    butterfly.delete_post(reply_data['uri'])

    # Now read the data of the post that you want to delete
    with open(POST_FILE, 'r') as post_file:
        post_data = yaml.load(post_file, Loader=yaml.FullLoader)

    # Delete the post
    butterfly.delete_post(post_data['uri'])
    ...
