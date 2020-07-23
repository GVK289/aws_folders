from fb_post.models import User, Post, Comment
from fb_post.exceptions import (InvalidUserException,
                                InvalidPostException,
                                InvalidCommentException,
                                InvalidReactionTypeException,
                                InvalidCommentContent,
                                InvalidPostContent,
                                UserCannotDeletePostException,
                                InvalidReplyContent)
from fb_post.constants import ReactionType


def check_whether_user_id_exists(user_id):
    user_is_invalid = not User.objects.filter(id=user_id)
    if user_is_invalid:
        raise InvalidUserException

def check_whether_post_id_exists(post_id):
    post_is_invalid = not Post.objects.filter(id=post_id)
    if post_is_invalid:
        raise InvalidPostException

def check_whether_comment_id_exists(comment_id):
    comment_is_invalid = not Comment.objects.filter(id=comment_id)
    if comment_is_invalid:
        raise InvalidCommentException
ReactionsList = [
    ReactionType.WOW.value,
    ReactionType.LIT.value,
    ReactionType.LOVE.value,
    ReactionType.HAHA.value,
    ReactionType.THUMBS_UP.value,
    ReactionType.THUMBS_DOWN.value,
    ReactionType.ANGRY.value,
    ReactionType.SAD.value
]


def check_whether_reaction_type_exists(reaction_type):
    reaction_type_not_in_reactions_list = reaction_type not in ReactionsList
    if reaction_type_not_in_reactions_list:
        raise InvalidReactionTypeException


def check_whether_comment_content_exists(comment_content):
    comment_content_is_invalid = not comment_content
    if comment_content_is_invalid:
        raise InvalidCommentContent


def check_whether_post_content_exists(post_content):
    post_content_is_invalid = not post_content
    if post_content_is_invalid:
        raise InvalidPostContent


def return_post_if_post_id_exists(post_id):
    check_whether_post_id_exists(post_id)
    post = Post.objects.get(id=post_id)
    return post


def check_whether_user_is_creator_of_post(posted_by, user_id):
    user_is_not_creator_of_post = posted_by != user_id
    if user_is_not_creator_of_post:
        raise UserCannotDeletePostException


def check_whether_reply_ccontent_exists(reply_content):
    reply_content_is_empty_or_none = not reply_content
    if reply_content_is_empty_or_none:
        raise InvalidReplyContent


def return_comment_if_comment_id_exists(comment_id):
    check_whether_comment_id_exists(comment_id)
    comment = Comment.objects.get(id=comment_id)
    return comment
