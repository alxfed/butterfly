# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
from configuration import go_configure, save_jwt
import yaml
from blue_yonder import Butterfly

# Path to the file where the list of posts will be stored.
POSTS_LIST_PATH = './data/posts_list.yaml'  # Path to the JWT file


if __name__ == "__main__":
    _, jwt = go_configure()

    butterfly = Butterfly(
        bluesky_handle=getenv('BLUESKY_HANDLE'),
        bluesky_password=getenv('BLUESKY_PASSWORD'),
        jwt=jwt
    )
    new_jwt = butterfly.publish_jwt()
    save_jwt(new_jwt)

    result = butterfly.get_posts_list()

    with open(POSTS_LIST_PATH, 'w') as posts_list_file:
        yaml.dump(result, posts_list_file)

    with open(POSTS_LIST_PATH, 'r') as posts_file:
        posts_list = yaml.load(posts_file, Loader=yaml.FullLoader)

    # Delete all posts if you are just experimenting.
    for post in posts_list['records']:
        butterfly.delete_post(post['uri'])

    final_result = butterfly.get_posts_list()

    # Record it in the file.
    with open(POSTS_LIST_PATH, 'w') as posts_list_file:
        yaml.dump(final_result, posts_list_file)
    ...