# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from blue_yonder import Another
import yaml

MEMBERS_FILE = 'data/mila_ai_list.yaml'
SHMEMBERS_FILE = 'data/mila_shlist.yaml'
person = Another(actor='josephdviviano.bsky.social')

lists = person.get_lists()
members = person.read_list(uri=lists[0]['uri'])
# shmembers = person.read_list(uri=lists[2]['uri'])

with open(MEMBERS_FILE, 'w') as list_file:
    yaml.dump(members, list_file)

# with open(SHMEMBERS_FILE, 'w') as list_file:
#     yaml.dump(shmembers, list_file)

...