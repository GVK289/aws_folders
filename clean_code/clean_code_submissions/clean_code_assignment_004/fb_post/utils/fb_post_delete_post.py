from fb_post.models import Post
from .fb_post_exception_methods import (
    check_whether_user_id_exists,
    return_post_if_post_id_exists,
    check_whether_user_is_creator_of_post
    )


def delete_post(user_id, post_id):
    check_whether_user_id_exists(user_id)
    post = return_post_if_post_id_exists(post_id)
    check_whether_user_is_creator_of_post(post.posted_by_id, user_id)

    post.delete()
