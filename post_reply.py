# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from blue_yonder import Actor
import yaml

POST_FILE = './data/post_data.yaml'  # The data about the post you've made, if you haven't execute the post_text.py program first.

reply_text = "This is true."


def main():
    my_actor = Actor()

    # If you have a URL of the post that you want to reply to, just uncomment this and change the URL to the one that you have.
    url = 'https://bsky.app/profile/alxfed.bsky.social/post/3lhjby65b5s2k'
    reply = (
        my_actor.in_reply_to(url)
        .post(reply_text)
    )

    # Or load the data of your first post (in posts_text.py) and use it.
    with open(POST_FILE, 'r') as post_file:
        post_data = yaml.load(post_file, Loader=yaml.FullLoader)

    # Post data has a 'uri' of that post in it.
    uri = post_data['uri']
    reply = (
        my_actor.in_reply_to(post_uri=uri)
        .post(reply_text)
    )


if __name__ == "__main__":
    main()
    ...