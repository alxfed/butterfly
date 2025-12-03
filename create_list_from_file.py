# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from blue_yonder import Actor
import yaml
from time import sleep

FILE_NAME = 'data/open_endedness.yaml'
LIST_NAME = 'OE'
LIST_DESCRIPTION = 'Open-endedness'
LIST_PROFILE_FILE = 'data/OE_list_profile.yaml'


with open(FILE_NAME, 'r') as list_file:
    members = yaml.load(list_file, Loader=yaml.BaseLoader)

my_actor = Actor(bluesky_handle='alxfed.bsky.social')
# created_list = my_actor.create_list(list_name=LIST_NAME, description=LIST_DESCRIPTION)
#
# with open(LIST_PROFILE_FILE, 'w') as save_file:
#     yaml.dump(created_list, save_file)

with open(LIST_PROFILE_FILE, 'r') as read_file:
    created_list = yaml.load(read_file, Loader=yaml.FullLoader)

list_uri = created_list['uri']
for member in members:
    member_did = member['subject']['did']
    my_actor.add_to_list(actor=member_did, list_uri=list_uri)
    sleep(2)
...