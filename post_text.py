# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
from configuration import go_configure, save_jwt
from blue_yonder import Butterfly

plain_text = """    This is an example of a plain text post.
A plain text post is a post that contains only text and no images. It is a simple way to post text to BlueSky. The maximum length of a plain text post is 290 characters. 
    Two hundred and ninety characters are pretty much enough if you . . .
"""


def main():
    """
    This is an example of a plain text post.
    """
    print(len(plain_text))  # let's check the length

    # if you don't want to set the environment variables
    # just store the credentials in the configuration file.
    # See the config_example.yaml

    config = go_configure()

    butterfly = Butterfly(
        bluesky_handle=getenv('BLUESKY_HANDLE', config[0]['BLUESKY_HANDLE']),
        bluesky_password=getenv('BLUESKY_PASSWORD', config[0]['BLUESKY_PASSWORD']),
        jwt=config[1]
    )

    updated_jwt = butterfly.publish_jwt()
    save_jwt(updated_jwt)

    result = butterfly.post(plain_text)

    return result


if __name__ == "__main__":
    main()
    ...
