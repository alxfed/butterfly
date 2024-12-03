# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import yaml
from blue_yonder import Client

# Make sure to have the environment variables set
# or uncomment the following lines
# import dotenv
# dotenv.load_dotenv()

JWT_PATH = './configuration/jwt.yaml'  # Path to the JWT file


def main():
    butterfly = Client()

    # The session parameters are in a JASON Web Token,
    # or jwt for short.
    jwt = butterfly.publish_jwt()

    # We will save it in a yaml file.
    with open(JWT_PATH, 'w') as jwt_file:
        yaml.dump(jwt, jwt_file)


def relogin():
    with open(JWT_PATH, 'r') as jwt_file:
        jwt = yaml.load(jwt_file, Loader=yaml.BaseLoader)

    # Instantiate the client with the old session (jwt).
    butterfly = Client(jwt=jwt)
    return butterfly


if __name__ == '__main__':
    main()
    butterfly = relogin()
    ...