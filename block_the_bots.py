# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import getenv
from configuration import load_jwt, save_jwt
from blue_yonder import Butterfly, Another
import yaml

butterfly = Butterfly(jwt=load_jwt())
save_jwt(butterfly.jwt)  # the .env file is loaded by PyCharm from elsewhere.

blocked_quote = 'https://bsky.app/profile/greene.haus/post/3lgjwjcvqyk26'

# another = Another(bluesky_handle='greene.haus')
with_quote = butterfly.read_post(blocked_quote)

rec = butterfly.block()
# rkey = rec['uri'].split("/")[-1]
result = butterfly.unblock(uri=rec['uri'], record_key=None)