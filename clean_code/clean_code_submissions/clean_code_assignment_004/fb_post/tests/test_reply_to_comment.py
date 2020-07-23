import datetime
import pytest
from freezegun import freeze_time
from fb_post.exceptions import InvalidUserException, InvalidCommentException
from fb_post.exceptions import InvalidReplyContent
from fb_post.models import Comment
from fb_post.utils import reply_to_comment


pytestmark = pytest.mark.django_db


def test_reply_to_comment_when_user_id_is_invalid_raises_invalid_user_exception(comment):
    # Arrange
    invalid_user_id = 100
    comment_id = 1
    reply_content = 'reply to comment1'

    # Act
    with pytest.raises(InvalidUserException):
        assert reply_to_comment(invalid_user_id, comment_id, reply_content)


def test_reply_to_comment_when_comment_id_is_invalid_raises_invalid_comment_exception(reply):
    # Arrange
    user_id = 1
    invalid_comment_id = 100
    reply_content = 'reply to comment1'

    # Act
    with pytest.raises(InvalidCommentException):
        assert reply_to_comment(user_id, invalid_comment_id, reply_content)


def test_reply_to_comment_when_reply_content_is_invalid_raises_invalid_reply_content_exception(reply):
    # Arrange
    user_id = 1
    comment_id = Comment.objects.filter(content='comment1')[0].id
    invalid_reply_content = ''

    # Act
    with pytest.raises(InvalidReplyContent):
        assert reply_to_comment(user_id, comment_id, invalid_reply_content)


@freeze_time("2009-01-16")
def test_reply_to_comment_if_comment_id_corresponds_to_reply_create_comment_object_returns_created_comment_object_id(reply):
    # Arrange
    user_id = 1
    comment_id = 7
    parent_comment_id = 1
    reply_content = 'reply to comment1'
    commented_at = datetime.datetime.now()

    # Act
    new_comment_id = reply_to_comment(user_id, comment_id, reply_content)

    # Assert
    comment_object = Comment.objects.get(id=new_comment_id)
    assert comment_object.commented_by_id == user_id
    assert comment_object.content == reply_content
    assert comment_object.parent_comment_id == parent_comment_id
    assert comment_object.commented_at.replace(tzinfo=None) == commented_at
