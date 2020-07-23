import datetime
import pytest
from freezegun import freeze_time
from fb_post.exceptions import InvalidUserException, InvalidPostContent
from fb_post.models import Post
from fb_post.utils import create_post


pytestmark = pytest.mark.django_db


def test_create_post_when_user_is_invalid_raises_invalid_user_exception(user):
    # Arrange
    invalid_user_id = 100
    post_content = 'post1'

    # Act
    with pytest.raises(InvalidUserException):
        assert create_post(invalid_user_id, post_content)


def test_create_post_when_post_content_is_invalid_raises_invalid_post_content_exception(user):
    # Arrange
    valid_user_id = 1
    post_content = ''

    # Act
    with pytest.raises(InvalidPostContent):
        assert create_post(valid_user_id, post_content)


@freeze_time("2009-01-14")
def test_create_post_with_valid_details_creates_post_object_and_returns_post_id(post):
    # Arrange
    user_id = 1
    post_content = 'post1'
    commented_at = datetime.datetime.now()

    # Act
    post_id = create_post(user_id, post_content)

    # Assert
    post_object = Post.objects.get(id=post_id)
    assert post_object.posted_by_id == user_id
    assert post_object.content == post_content
    assert post_object.posted_at.replace(tzinfo=None) == commented_at
