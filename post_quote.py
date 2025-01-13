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

plain_text_reply = """    This is an example of a plain text reply to a post.
"""

POST_FILE = './data/post_data.yaml'
REPLY_FILE = './data/reply_data.yaml'


if __name__ == "__main__":
    """
    This is an example of a plain text reply.
    """

    butterfly = Butterfly(jwt=load_jwt())
    save_jwt(butterfly.jwt)

    # Read the data of the post that we want to reply to
    with open(POST_FILE, 'r') as post_file:
        post_data = yaml.load(post_file, Loader=yaml.FullLoader)

    # Now, post the reply
    result = butterfly.reply(root_post=post_data, post=post_data, text=plain_text_reply)

    # We will store the reply data in a yaml file too.
    with open(REPLY_FILE, 'w') as reply_file:
        yaml.dump(result, reply_file)

    with open(REPLY_FILE, 'r') as reply_file:
        reply_data = yaml.load(reply_file, Loader=yaml.FullLoader)
    ...
