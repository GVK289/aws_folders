import datetime
import pytest
from freezegun import freeze_time
from fb_post.exceptions import InvalidUserException, InvalidPostException
from fb_post.exceptions import InvalidCommentContent
from fb_post.models import Comment
from fb_post.utils import create_comment


pytestmark = pytest.mark.django_db


def test_create_comment_when_user_id_is_invalid_raises_invalid_user_exception(post):
    # Arrange
    invalid_user_id = 100
    post_id = 1
    comment_content = 'comment1'

    # Act
    with pytest.raises(InvalidUserException):
        assert create_comment(invalid_user_id, post_id, comment_content)


def test_create_comment_when_post_id_is_invalid_raises_invalid_post_exception(post):
    # Arrange
    user_id = 1
    invalid_post_id = 100
    comment_content = 'comment1'

    # Act
    with pytest.raises(InvalidPostException):
        assert create_comment(user_id, invalid_post_id, comment_content)


def test_create_comment_when_comment_content_is_invalid_raises_invalid_comment_content_exception(post):
    # Arrange
    user_id = 1
    post_id = 1
    invalid_comment_content = ''

    # Act
    with pytest.raises(InvalidCommentContent):
        assert create_comment(user_id, post_id, invalid_comment_content)


@freeze_time("2010-01-14")
def test_create_comment_when_valid_user_id_and_comment_content_are_given_creates_comment_object_and_returns_comment_id(post):
    # Arrange
    user_id = 1
    post_id = 1
    comment_content = 'comment1'
    commented_at = datetime.datetime.now()

    # Act
    create_comment(user_id, post_id, comment_content)

    # Assert
    comment_object = Comment.objects.get(commented_by_id=user_id,
                                         post_id=post_id)
    assert comment_object.commented_by_id == user_id
    assert comment_object.post_id == post_id
    assert comment_object.content == comment_content
    assert comment_object.commented_at.replace(tzinfo=None) == commented_at
