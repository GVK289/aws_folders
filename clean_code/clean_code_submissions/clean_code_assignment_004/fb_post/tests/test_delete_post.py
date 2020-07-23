import pytest
from fb_post.exceptions import InvalidUserException, InvalidPostException
from fb_post.exceptions import UserCannotDeletePostException
from fb_post.models import Post
from fb_post.utils import delete_post


pytestmark = pytest.mark.django_db


def test_delete_post_when_user_id_is_invalid_raises_invalid_user_exception(post):
    # Arrange
    user_id = 100
    post_id = 2

    # Act
    with pytest.raises(InvalidUserException):
        assert delete_post(user_id, post_id)


def test_delete_post_when_post_id_is_invalid_raises_invalid_post_exception(post):
    # Arrange
    user_id = 1
    post_id = 200

    # Act
    with pytest.raises(InvalidPostException):
        assert delete_post(user_id, post_id)


@pytest.mark.parametrize('user_id, post_id', [(5, 1), (1, 5)])
def test_delete_post_when_user_is_not_the_creator_of_post_raises_user_cannot_delete_post_exception(user_id, post_id, post):
    # Act
    with pytest.raises(UserCannotDeletePostException):
        assert delete_post(user_id, post_id)


def test_delete_post_when_user_is_the_creator_of_post_delete_the_post_object(post):
    # Arrange
    user_id = 1
    post_id = 1

    # Act
    delete_post(user_id, post_id)

    # Assert
    post_object = Post.objects.filter(id=post_id, posted_by_id=user_id)
    assert post_object.exists() is False
