import pytest
from fb_post.exceptions import InvalidPostException
from fb_post.utils import get_reactions_to_post


pytestmark = pytest.mark.django_db


def test_get_reactions_to_post_when_post_id_is_invalid_raises_invalid_post_exception(reaction):
    # Arrange
    invalid_post_id = 100

    # Act
    with pytest.raises(InvalidPostException):
        assert get_reactions_to_post(invalid_post_id)


def test_get_reactions_to_post_if_post_has_reactions_returns_list_of_dictionaries_of_user_details_of_post(reaction):
    # Arrange
    post_id = 1
    list_user_details_of_post_dict = [
        {"user_id": 2, "name": "user2", "profile_pic": "user2_pic",
         "reaction": "WOW"},
        {"user_id": 3, "name": "user3", "profile_pic": "user3_pic",
         "reaction": "LIT"}
        ]

    # Act
    list_of_user_and_reactions_dict = get_reactions_to_post(post_id)

    # Asset
    assert list_user_details_of_post_dict == list_of_user_and_reactions_dict


def test_get_reactions_to_post_if_post_has_no_reactions_returns_empty_list(reaction):
    # Arrange
    post_id = 5
    list_of_user_details_of_post = []

    # Act
    list_of_user_and_reactions_dict = get_reactions_to_post(post_id)

    # Asset
    assert list_of_user_details_of_post == list_of_user_and_reactions_dict
