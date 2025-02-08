# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
from configuration import go_configure, load_jwt, save_jwt
from blue_yonder import Actor
import yaml

reply_text = """    This is an example of a reply to a post that has an embedded
quote of another post.
"""
post = 'https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l'

POST_FILE = './data/post_data.yaml'


def main():
    """ Quote a Bluesky post.
    :return:
    """
    my_actor = Actor(jwt=load_jwt())
    save_jwt(my_actor.jwt)

    url = 'https://bsky.app/profile/multilogue.bsky.social/post/3lfngdvswe725'

    # Now, post it!
    reply = my_actor.in_reply_to(url).with_quoted_post(post).post(reply_text)

    # We can store the post data in a yaml file
    with open(POST_FILE, 'w') as post_file:
        yaml.dump(reply, post_file)

    with open(POST_FILE, 'r') as post_file:
        post_data = yaml.load(post_file, Loader=yaml.FullLoader)


if __name__ == "__main__":
    """ This is an example of a reply to a post with a quote in it.
    """
    main()
    ... # A line for setting a breakpoint in IDE.
