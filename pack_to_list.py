# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from blue_yonder import Another
import yaml

MEMBERS_FILE = 'data/open_endedness.yaml'
person = Another(actor='rockt.ai')

stp = 'https://bsky.app/starter-pack/rockt.ai/3lazblsf4z72k'

lists = person.get_lists()
members = person.read_list(uri=lists[0]['uri'])

with open(MEMBERS_FILE, 'w') as list_file:
    yaml.dump(members, list_file)

# with open(SHMEMBERS_FILE, 'w') as list_file:
#     yaml.dump(shmembers, list_file)

...