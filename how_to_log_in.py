# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import yaml
from blue_yonder import Actor

handle = '<your username>.bsky.social' # your bluesky handle in this format here
password = 'password' # your bluesky password here


def log_in():
    """ Log-in to the BlueSky API / service using your handle and password.
    """
    my_actor = Actor(bluesky_handle=handle,
                     bluesky_password=password)

    # But it is better to have the environment variables set
    # in an .env file that is loaded by PyCharm or other IDE.
    # There is a .env_example file in this folder.
    #
    # If you don't know how to do it or are using *.ipynb
    # create the same.env file and do the following:
    import dotenv
    dotenv.load_dotenv()

    # After that you can just call the Actor class without any
    # arguments to log in.
    my_actor = Actor()

    # Yet another way to log-in is to use the config.yaml file.
    # See the config_example.yaml
    # Then do:
    from os import getenv
    from configuration import go_configure, load_jwt

    config = go_configure(config_file='config_example.yaml')

    my_actor = Actor(
        bluesky_handle=config['BLUESKY_HANDLE'],
        bluesky_password=config['BLUESKY_PASSWORD']
    )

    # or a combination of environment variables and config file
    from os import getenv

    my_actor = Actor(
        bluesky_handle=getenv('BLUESKY_HANDLE', config['BLUESKY_HANDLE']),
        bluesky_password=getenv('BLUESKY_PASSWORD', config['BLUESKY_PASSWORD'])
    )

    return my_actor


if __name__ == '__main__':
    my_actor = log_in()
    ...  # A line for setting a breakpoint in your IDE
