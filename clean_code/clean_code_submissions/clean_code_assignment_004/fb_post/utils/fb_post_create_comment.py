from fb_post.models import Comment
from .fb_post_exception_methods import (
    check_whether_user_id_exists,
    check_whether_post_id_exists,
    check_whether_comment_content_exists
    )


# Task 03
def create_comment(user_id, post_id, comment_content):
    check_whether_user_id_exists(user_id)
    check_whether_post_id_exists(post_id)
    check_whether_comment_content_exists(comment_content)

    new_comment_object = (Comment.objects
                          .create(commented_by_id=user_id,
                                  post_id=post_id,
                                  content=comment_content))
    return new_comment_object.id
