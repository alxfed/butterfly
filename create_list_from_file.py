# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from blue_yonder import Actor
import yaml
from time import sleep

FILE_NAME = 'data/mila_ai_list.yaml'
# SHFILE_NAME = 'data/hf_adm_list.yaml'
LIST_NAME = 'MILA'
LIST_DESCRIPTION = 'Mila AI'
LIST_PROFILE_FILE = 'data/mila_ai_list_profile.yaml'


with open(FILE_NAME, 'r') as list_file:
    members = yaml.load(list_file, Loader=yaml.BaseLoader)

# with open(SHFILE_NAME, 'r') as list_file:
#     shmembers = yaml.load(list_file, Loader=yaml.BaseLoader)

# members.extend(shmembers)

my_actor = Actor()
created_list = my_actor.create_list(list_name=LIST_NAME, description=LIST_DESCRIPTION)

with open(LIST_PROFILE_FILE, 'w') as save_file:
    yaml.dump(created_list, save_file)

list_uri = created_list['uri']
for member in members:
    member_did = member['subject']['did']
    # if member['subject']['handle'] == 'mcmozer.bsky.social':
    #     pass
    my_actor.add_to_list( actor=member_did, list_uri=list_uri,)
    sleep(2)

...