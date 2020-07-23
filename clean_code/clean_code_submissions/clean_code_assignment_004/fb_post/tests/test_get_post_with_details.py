import pytest
from fb_post.exceptions import InvalidPostException
from fb_post.constants import ReactionType
from fb_post.utils import get_post
from .check_returned_and_excepted_arguments import check_posts

pytestmark = pytest.mark.django_db


def test_get_post_when_post_having_comments_reaction_to_comments_and_post_reactions_returns_post_details_and_posts_commentes_and_reactions_returns_dictionary(reaction, reply, reaction_to_comments):
    # Arrange
    post_id = 1
    expected = {
        'post_id': 1,
        'posted_by': {
            'name': 'user1',
            'user_id': 1,
            'profile_pic': 'user1_pic'
        },
        'posted_at': "2012-09-10 00:00:00.000000",
        'post_content': 'post1',
        'reactions': {
            'count': 2,
            'type': [
                ReactionType.WOW.value,
                ReactionType.LIT.value
            ]
        },
        'comments': [
            {
                'comment_id': 1,
                'commenter': {
                    'user_id': 1,
                    'name': 'user1',
                    'profile_pic': 'user1_pic'
                },
                'commented_at': "2012-09-10 00:00:00.000000",
                'comment_content': 'comment1',
                'reactions': {
                    'count': 3,
                    'type': [
                        ReactionType.LIT.value,
                        ReactionType.THUMBS_DOWN.value
                    ]
                },
                'replies_count': 1,
                'replies': [{
                    'comment_id': 7,
                    'commenter':{
                        'user_id': 2,
                        'name': 'user2',
                        'profile_pic': 'user2_pic'
                    },
                    'commented_at': "2012-09-10 00:00:00.000000",
                    'comment_content': 'reply_to_comment1 by 2',
                    'reactions': {
                        'count': 0,
                        'type': []
                    }
                }]
                
            },
            {
                'comment_id': 3,
                'commenter': {
                    'user_id': 2,
                    'name': 'user2',
                    'profile_pic': 'user2_pic'
                },
                'commented_at': "2012-09-10 00:00:00.000000",
                'comment_content': 'comment1',
                'reactions': {
                    'count': 1,
                    'type': [ReactionType.ANGRY.value]
                },
                'replies_count': 0,
                'replies': []
            },
            {
                'comment_id': 4,
                'commenter': {
                    'user_id': 3,
                    'name': 'user3',
                    'profile_pic': 'user3_pic'
                },
                'commented_at': "2012-09-10 00:00:00.000000",
                'comment_content': 'comment2',
                'reactions': {
                    'count': 1,
                    'type': [ReactionType.THUMBS_UP.value]
                },
                'replies_count': 1,
                'replies': [
                    {
                        'comment_id': 10,
                        'commenter': {
                            'user_id': 1,
                            'name': 'user1',
                            'profile_pic': 'user1_pic'
                        },
                        'commented_at': "2012-09-10 00:00:00.000000",
                        'comment_content': 'reply_to_comment4 by 1',
                        'reactions': {
                            'count': 0,
                            'type': []
                        }
                    }
                ]
            }
        ],
        'comments_count': 3
    }

    # Act
    returned = get_post(post_id)

    # Assert
    assert check_posts(returned, expected)
