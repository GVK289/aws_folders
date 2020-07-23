from fb_post.models import Post
from .fb_post_exception_methods import (
    check_whether_user_id_exists,
    check_whether_post_content_exists
    )


# Task 02
def create_post(user_id, post_content):
    check_whether_user_id_exists(user_id)
    check_whether_post_content_exists(post_content)

    new_post_object = Post.objects.create(posted_by_id=user_id,
                                          content=post_content)
    return new_post_object.id
