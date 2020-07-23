from fb_post.models import Comment
from .fb_post_exception_methods import (check_whether_user_id_exists,
                                        check_whether_reply_ccontent_exists,
                                        return_comment_if_comment_id_exists)


def reply_to_comment(user_id, comment_id, reply_content):
    check_whether_user_id_exists(user_id)
    comment = return_comment_if_comment_id_exists(comment_id)
    check_whether_reply_ccontent_exists(reply_content)
    parent_comment_id_is_not_none = comment.parent_comment_id != None
    if parent_comment_id_is_not_none:
        comment_id = comment.parent_comment_id
    new_comment_object = (Comment.objects
                          .create(commented_by_id=user_id,
                                  post_id=comment.post_id,
                                  parent_comment_id=comment_id,
                                  content=reply_content))
    return new_comment_object.id
