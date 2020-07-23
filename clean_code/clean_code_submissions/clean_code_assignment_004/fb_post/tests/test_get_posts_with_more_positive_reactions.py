import pytest
from fb_post.utils import get_posts_with_more_positive_reactions


pytestmark = pytest.mark.django_db


def test_get_posts_with_more_positive_reactions_if_positive_reactions_of_post_greater_than_negative_reactions_of_post_returns_post_ids_of_posts_in_list(reaction):
    # Arrange
    post_ids_list = [1, 3]

    # Act
    list_of_post_ids = get_posts_with_more_positive_reactions()

    # Assert
    assert post_ids_list == list_of_post_ids


def test_get_posts_with_more_positive_reactions_if_positive_reactions_of_post_not_greater_than_negative_reactions_of_post_returns_empty_list():
    # Arrange
    post_ids_list = []

    # Act
    list_of_post_ids = get_posts_with_more_positive_reactions()

    # Assert
    assert post_ids_list == list_of_post_ids
