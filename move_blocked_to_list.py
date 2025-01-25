# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from time import sleep
from configuration import load_jwt, save_jwt
from blue_yonder import Butterfly, Another
import yaml

BLOCKED_PEOPLE_FILE = './data/blocked_list.yaml'

butterfly = Butterfly(bluesky_handle='alxfed.bsky.social', jwt=load_jwt())
save_jwt(butterfly.jwt)  # the .env file is loaded by PyCharm from elsewhere.

list_of_blocked_rec = butterfly._records(collection='app.bsky.graph.block')
with open(BLOCKED_PEOPLE_FILE, 'w') as list_file:
    yaml.dump(list_of_blocked_rec, list_file)

with open(BLOCKED_PEOPLE_FILE, 'r') as list_file:
    members = yaml.load(list_file, Loader=yaml.BaseLoader)

""" Go to the 'moderation' section of your settings then to 'moderation lists'.
Create and join one, with 'block' property, then copy its URL here. """

mod_list_url = 'https://bsky.app/profile/alxfed.bsky.social/lists/3lfkcljp7fh23'

mod_list_uri = butterfly.uri_from_url(mod_list_url)

for member_record in members:
    member_did = member_record['value']['subject']
    # who = Another(actor=member_did)
    result = butterfly.unblock(uri=member_record['uri'])
    butterfly.add_to_list(actor=member_did, list_uri=mod_list_uri, )
    sleep(2)

...
