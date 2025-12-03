# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from time import sleep
from blue_yonder import Actor, yonder
import yaml

FOUND_PEOPLE_FILE = './data/found_people.yaml'
LIST_URL = 'https://bsky.app/profile/alxfed.bsky.social/lists/3ldckd6tqsk2j'  # GDM
LIST_URI = 'at://did:plc:x7lte36djjyhereki5avyst7/app.bsky.graph.list/3lfxoqfun6v2q'


def main():
    people = yonder.search_actors(query={'q': 'AI', 'limit': 50}, max_results=1000)

    # We will store the reply data in a yaml file too.
    with open(FOUND_PEOPLE_FILE, 'w') as found_people_file:
        yaml.dump(people, found_people_file)

    with open(FOUND_PEOPLE_FILE, 'r') as found_people_file:
        people = yaml.load(found_people_file, Loader=yaml.FullLoader)

    my_actor = Actor(bluesky_handle='alxfed.bsky.social')
    # LIST_URI, did, handle, rkey = my_actor.uri_from_url(LIST_URL)
    # lists = my_actor.get_lists()

    for member in people:
        member_did = member['did']
        my_actor.add_to_list(actor=member_did, list_url=LIST_URL)
        sleep(2)
        # and don't browse the list when it is happening! it will cause 502 error.


if __name__ == "__main__":
    main()
    ...