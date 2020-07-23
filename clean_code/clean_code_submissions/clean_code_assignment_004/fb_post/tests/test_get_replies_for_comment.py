import pytest
from fb_post.exceptions import InvalidCommentException
from fb_post.utils import get_replies_for_comment


pytestmark = pytest.mark.django_db


def test_get_replies_for_comment_when_comment_id_is_invalid_raises_invalid_comment_exception(reply):
    #  Arrange
    comment_id = 100

    # Act
    with pytest.raises(InvalidCommentException):
        assert get_replies_for_comment(comment_id)


def test_get_replies_for_comment_with_valid_comment_id_returns_list_of_dictionaries_of_comment_details_with_commenter_details(reply):
    # Arrange
    comment_id = 1
    list_of_dict_of_comment_details = [
        {
            'comment_id': 7,
            'commenter': {'user_id': 2, 'name': 'user2',
                          'profile_pic': 'user2_pic'},
            'commented_at': "2012-09-10 00:00:00.000000",
            'comment_content': 'reply_to_comment1 by 2'}]

    # Act
    get_list_of_comment_details_dict = get_replies_for_comment(comment_id)

    # Assert
    assert list_of_dict_of_comment_details == get_list_of_comment_details_dict


def test_get_replies_for_comment_with_valid_comment_id_having_no_replies_returns_empty_list(reply):
    # Arrange
    comment_id = 7
    list_of_dict_of_comment_details = []

    # Act
    get_list_of_comment_details_dict = get_replies_for_comment(comment_id)

    # Assert
    assert list_of_dict_of_comment_details == get_list_of_comment_details_dict
