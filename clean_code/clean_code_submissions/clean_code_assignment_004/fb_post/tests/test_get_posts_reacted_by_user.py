import pytest
from fb_post.exceptions import InvalidUserException
from fb_post.utils import get_posts_reacted_by_user


pytestmark = pytest.mark.django_db


def test_get_posts_reacted_by_user_when_user_id_is_invalid_raises_invalid_user_exception(reaction):
    # Arrange
    user_id = 100

    # Act
    with pytest.raises(InvalidUserException):
        assert get_posts_reacted_by_user(user_id)


def test_get_posts_reacted_by_user_when_user_reacts_to_posts_returns_post_ids_of_user_reacted_posts_in_list(reaction):
    # Arrange
    user_id = 2
    post_ids_list = [1, 3]

    # Act
    list_of_post_ids = get_posts_reacted_by_user(user_id)

    # Assert
    assert post_ids_list == list_of_post_ids


def test_get_posts_reacted_by_user_when_user_does_not_react_to_any_posts_returns_empty_list(reaction):
    # Arrange
    user_id = 1
    post_ids_list = []

    # Act
    list_of_post_ids = get_posts_reacted_by_user(user_id)

    # Assert
    assert post_ids_list == list_of_post_ids
