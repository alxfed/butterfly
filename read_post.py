# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from blue_yonder import Actor

post = 'https://bsky.app/profile/hardmaru.bsky.social/post/3lfr3exrpas2d'


def main():
    my_actor = Actor()
    post_data = my_actor.read_post(post)
    # embed of $type = 'app.bsky.embed.recordWithMedia'
    #    media:
    #        $type: 'app.bsky.embed.images',
    #        images: [ <blobs> ]
    #    record:
    #        $type: 'app.bsky.embed.record'
    #        record: {uri:, cid:}
    ...


if __name__ == '__main__':
    main()
    ...