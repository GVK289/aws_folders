# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_post_with_valid_details post_details'] = {
    'comments': [
    ],
    'comments_count': 0,
    'post_content': 'post content of post0',
    'post_id': 1,
    'posted_at': '2012-09-10 00:00:00.000000',
    'posted_by': {
        'name': 'vinay5',
        'profile_pic': 'vinay5@example.com',
        'user_id': 6
    },
    'reactions': {
        'count': 0,
        'type': [
        ]
    }
}

snapshots['test_get_post_with_valid_details resultant_post_id'] = 1

snapshots['test_get_post_with_valid_details resultant_posted_by'] = {
    'name': 'vinay5',
    'profile_pic': 'vinay5@example.com',
    'user_id': 6
}

snapshots['test_get_post_with_valid_details resultant_posted_at'] = '2012-09-10 00:00:00.000000'

snapshots['test_get_post_with_valid_details resultant_comments'] = [
]
