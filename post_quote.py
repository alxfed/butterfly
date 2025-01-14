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

plain_text = """    This is an example of a plain text post with a quote. The URL of the post that should be quoted can point at any Bluesky post, be it a plain text, image or post with a link to an extarnal page/site.
"""
url = 'https://bsky.app/profile/bsky.app/post/3l6oveex3ii2l'

POST_FILE = './data/post_data.yaml'


def main():
    """ Quote a Bluesky post.
    :return:
    """
    my_actor = Actor(jwt=load_jwt())
    save_jwt(my_actor.jwt)

    # Now, post the text
    result = my_actor.quote_post(plain_text, quote_url=url)

    # We can store the post data in a yaml file
    with open(POST_FILE, 'w') as post_file:
        yaml.dump(result, post_file)

    with open(POST_FILE, 'r') as post_file:
        post_data = yaml.load(post_file, Loader=yaml.FullLoader)


if __name__ == "__main__":
    """ This is an example of a plain text post.
    """
    print(len(plain_text))  # let's check the length

    # if you don't want to set the environment variables
    # just store the credentials in the configuration file.
    # See the config_example.yaml
    # Then do:
    # config = go_configure(config_file='config_example.yaml')
    #
    # butterfly = Actor(
    #     bluesky_handle=getenv('BLUESKY_HANDLE', config['BLUESKY_HANDLE']),
    #     bluesky_password=getenv('BLUESKY_PASSWORD', config['BLUESKY_PASSWORD']),
    #     jwt=load_jwt()
    # )
    # save_jwt(butterfly.jwt())

    main()
    ... # A line for setting a breakpoint in IDE.
