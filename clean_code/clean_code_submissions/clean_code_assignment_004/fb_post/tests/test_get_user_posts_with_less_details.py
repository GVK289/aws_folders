import pytest
from fb_post.exceptions import InvalidPostException, InvalidUserException
from fb_post.constants import ReactionType
from fb_post.utils import get_user_posts
from .check_returned_and_excepted_arguments import (
    is_excepted_and_returned_output_of_posts_equal)


pytestmark = pytest.mark.django_db


def test_get_user_posts_when_user_id_is_invalid_raises_invalid_user_exception(post):
    # Arrange
    invalid_user_id = 100

    # Act
    with pytest.raises(InvalidUserException) :
        assert get_user_posts(invalid_user_id)


def test_get_user_posts_when_user_has_posts_returns_list_of_dictionaries_of_post_details_of_user(reaction, reaction_to_comments):
    # Arrange
    user_id = 1
    expected = [
            {'post_id': 1,
                'posted_by': {'user_id': 1,
                              'name': 'user1',
                              'profile_pic': 'user1_pic'},
                'posted_at': '2012-09-10 00:00:00.000000',
                'post_content': 'post1',
                'reactions': {'count': 2,
                              'type': [ReactionType.WOW.value,
                                       ReactionType.LIT.value]},
                'comments': [
                    {
                    'comment_id': 1,
                        'commenter': {'user_id': 1,
                                      'name': 'user1',
                                      'profile_pic': 'user1_pic'},
                        'commented_at': '2012-09-10 00:00:00.000000',
                        'comment_content': 'comment1',
                        'reactions': {'count': 3,
                                      'type': [ReactionType.LIT.value,
                                               ReactionType.THUMBS_DOWN.value]
                                     },
                        'replies_count': 0,
                        'replies': []
                    },
                    {'comment_id': 3,
                        'commenter': {'user_id': 2,
                                      'name': 'user2',
                                      'profile_pic': 'user2_pic'},
                        'commented_at': '2012-09-10 00:00:00.000000',
                        'comment_content': 'comment1',
                        'reactions': {'count': 1,
                                      'type': [ReactionType.ANGRY.value]},
                        'replies_count': 0,
                        'replies': []
                    },
                    {'comment_id': 4, 
                        'commenter': {'user_id': 3,
                                      'name': 'user3',
                                      'profile_pic': 'user3_pic'},
                        'commented_at': '2012-09-10 00:00:00.000000',
                        'comment_content': 'comment2',
                        'reactions': {'count': 1,
                                      'type': [ReactionType.THUMBS_UP.value]},
                        'replies_count': 0,
                        'replies': []
                    }
                ],
                'comments_count': 3
            },
            {'post_id': 2,
                'posted_by': {'user_id': 1,
                              'name': 'user1',
                              'profile_pic': 'user1_pic'},
                'posted_at': '2012-09-10 00:00:00.000000',
                'post_content': 'post2',
                'reactions': {'count': 1, 'type': [ReactionType.SAD.value]},
                'comments': [
                    {'comment_id': 2,
                        'commenter': {'user_id': 1,
                                      'name': 'user1',
                                      'profile_pic': 'user1_pic'},
                        'commented_at': '2012-09-10 00:00:00.000000',
                        'comment_content': 'comment2',
                        'reactions': {'count': 1,
                                      'type': [ReactionType.SAD.value]},
                        'replies_count': 0,
                        'replies': []
                    },
                    {'comment_id': 5,
                        'commenter': {'user_id': 3,
                                      'name': 'user3',
                                      'profile_pic': 'user3_pic'},
                        'commented_at': '2012-09-10 00:00:00.000000',
                        'comment_content': 'comment3',
                        'reactions': {'count': 0, 'type': []},
                        'replies_count': 0,
                        'replies': []
                    }
                ],
                'comments_count': 2}
            ]

    # Act
    returned = get_user_posts(user_id)

    # Assert
    assert is_excepted_and_returned_output_of_posts_equal(returned, expected)

def test_get_user_posts_when_user_does_not_posts_returns_empty_list(user):
    # Arrange
    user_id = 2
    user_posts_list_excpected = []

    # Act
    list_of_user_posts = get_user_posts(user_id)

    # Assert
    assert user_posts_list_excpected == list_of_user_posts
