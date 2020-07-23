import pytest
from fb_post.exceptions import InvalidPostException
from fb_post.constants import ReactionType
from fb_post.utils import get_post
#check_returned_and_excepted_arguments


pytestmark = pytest.mark.django_db


def test_get_post_when_post_id_is_invalid_raises_invalid_post_exception(reaction, reply, reaction_to_comments):
    # Arrange
    invalid_post_id = 100

    # Act
    with pytest.raises(InvalidPostException):
        assert get_post(invalid_post_id)


def test_get_post_when_post_having_no_comments_and_reactions_returns_post_details_and_post_user_details_returns_dictionary(post):
    # Arrange
    post_id = 1
    post_dict = {
        'post_id': 1,
        'posted_by': {
            'user_id': 1,
            'name': 'user1',
            'profile_pic': 'user1_pic'
        },
        'posted_at': '2012-09-10 00:00:00.000000',
        'post_content': 'post1',
        'reactions': {'count': 0, 'type': []},
        'comments': [],
        'comments_count': 0,
    }

    # Act
    dict_of_post_details = get_post(post_id)

    # Assert
    assert post_dict == dict_of_post_details

def test_get_post_when_there_are_no_commentes_for_posts_returns_empty_list_with_post_details_in_dictionary(reaction):
    # Arrange
    post_id = 1
    post_dict = {
          'post_id': 1,
          'posted_by': {
                'user_id': 1,
                'name': 'user1',
                'profile_pic': 'user1_pic'
                },
          'posted_at': '2012-09-10 00:00:00.000000',
          'post_content': 'post1',
          'reactions': {'count': 2, 'type': [ReactionType.WOW.value,
                                             ReactionType.LIT.value]},
          'comments': [],
          'comments_count': 0,
          }

    # Act
    dict_of_post_details = get_post(post_id)

    # Assert
    assert post_dict == dict_of_post_details

def test_get_post_when_there_are_no_reactions_for_posts_returns_dictionary_with_count_value_zero_and_type_with_empty_list_and_post_details_in_dictionary(comment):
    # Arrange
    post_id = 1
    post_dict = {
        'post_id': 1,
        'posted_by': {
            'user_id': 1,
            'name': 'user1', 
            'profile_pic': 'user1_pic'
        },
        'posted_at': '2012-09-10 00:00:00.000000',
        'post_content': 'post1',
        'reactions': {
            'count': 0,
            'type': []
        },
        'comments':[
            {
                'comment_id': 1,
                'commenter': {
                    'user_id': 1,
                    'name': 'user1',
                    'profile_pic': 'user1_pic',
                },
                'commented_at': '2012-09-10 00:00:00.000000',
                'comment_content': 'comment1',
                'reactions': {
                    'count': 0,
                    'type': []
                },
                'replies': [],
                'replies_count': 0
            },
            {
                'comment_id': 3,
                'commenter': {
                    'user_id': 2,
                    'name': 'user2',
                    'profile_pic': 'user2_pic',
                },
                'commented_at': '2012-09-10 00:00:00.000000',
                'comment_content': 'comment1',
                'reactions': {
                    'count': 0,
                    'type': []
                },
                'replies': [],
                'replies_count': 0
            },
            {
                'comment_id': 4,
                'commented_at': '2012-09-10 00:00:00.000000',
                'comment_content': 'comment2',
                'commenter': {
                    'user_id': 3,
                    'name': 'user3',
                    'profile_pic': 'user3_pic',
                },
                'reactions': {
                    'count': 0,
                    'type': []
                },
                'replies': [],
                'replies_count': 0
            }
        ],
        'comments_count': 3,
    }

    # Act
    dict_of_post_details = get_post(post_id)

    # Assert
    assert post_dict == dict_of_post_details 

