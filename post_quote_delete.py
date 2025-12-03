# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from configuration import load_jwt, save_jwt
from blue_yonder import Actor
import yaml

plain_text = """    This is an example of a plain text post.
It will be quoted in another post. 
"""
plain_text_with_quote = """    This is an example of a plain text post quoting another plain text post.
"""

POST_FILE = './data/post_data.yaml'
POST_WITH_QUOTE_FILE = './data/post_with_quote_data.yaml'


if __name__ == "__main__":
    """
    This is an example of a plain text post.
    """
    print(len(plain_text))  # let's check the length

    my_actor = Actor(jwt=load_jwt())
    save_jwt(my_actor.jwt)

    # Now, post the text
    result = my_actor.post(plain_text)

    # We will store the post data in a yaml file
    with open(POST_FILE, 'w') as post_file:
        yaml.dump(result, post_file)

    # Read the post data
    with open(POST_FILE, 'r') as post_file:
        post_data = yaml.load(post_file, Loader=yaml.FullLoader)

    # Now, post the quote
    result = my_actor.quote_post(embed_post=post_data, text=plain_text_with_quote)

    # We will store the reply data in a yaml file too.
    with open(POST_WITH_QUOTE_FILE, 'w') as post_with_quote_file:
        yaml.dump(result, post_with_quote_file)

    """ Look at your bluesky profile and you will see the post and reply.
        Now we can delete the reply and the post.
    """

    # Read the data of the reply that you want to delete
    with open(POST_WITH_QUOTE_FILE, 'r') as post_with_quote_file:
        reply_data = yaml.load(post_with_quote_file, Loader=yaml.FullLoader)

    # Now, delete the reply
    my_actor.delete_post(reply_data['uri'])

    # Now read the data of the post that you want to delete
    with open(POST_FILE, 'r') as post_file:
        post_data = yaml.load(post_file, Loader=yaml.FullLoader)

    # Delete the post
    my_actor.delete_post(post_data['uri'])
    ...
