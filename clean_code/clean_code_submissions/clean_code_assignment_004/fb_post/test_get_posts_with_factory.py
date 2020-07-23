import unittest
import pytest
from fb_post.exceptions import InvalidPostException
from fb_post.constants import ReactionType
from fb_post.utils import get_post
from fb_post.models import User, Post
from freezegun import freeze_time
from .factory_sample import *


#@freeze_time("2012-09-10 00:00:00.00")
@pytest.fixture
def user_objects():
    UserFactory.create_batch(size=5)


@pytest.fixture
@freeze_time("2012-09-10 00:00:00.00")
def post_objects():
    PostFactory.create_batch(size=3)


@pytest.fixture
@freeze_time("2012-09-10 00:00:00.00")
def comment_objects():
    PostCommentFactory.create_batch(size=2)
    ReplyCommentFactory.create_batch(size=2)


@pytest.fixture
@freeze_time("2012-09-10 00:00:00.00")
def reaction_bjects():
    PostReactionsFactory.create_batch(size=2)
    CommentReactionsFactory.create_batch(size=2)
    ReplyCommentReactionsFactory.create_batch(size=1)


pytestmark = pytest.mark.django_db


def test_get_post_with_valid_details(
        user_objects, post_objects,
        comment_objects, reaction_bjects,
        snapshot):
    # Arrange
    post_id = 1

    # Act
    dict_of_post_details = get_post(post_id)

    # Assert
    snapshot.assert_match(
        dict_of_post_details['post_id'], 'resultant_post_id')
    snapshot.assert_match(
        dict_of_post_details['posted_by'], 'resultant_posted_by')
    snapshot.assert_match(
        dict_of_post_details['posted_at'], 'resultant_posted_at')
    snapshot.assert_match(
        dict_of_post_details['comments'], 'resultant_post_comments')
    snapshot.assert_match(
        dict_of_post_details['comments_count'],
        'resultant_post_comments_count')
    

def _check_assert_of_comments_objects_list(comments, snapshot):
    for comment in comments:
        snapshot.assert_match(
            comment['comment_id'], 'resultant_post_comment_id')
        snapshot.assert_match(
            comment['commented_at'], 'resultant_post_commented_at')
        snapshot.assert_match(
            comment['comment_conent'], 'resultant_post_comment_content')
        
        