from django.db.models import Prefetch
from fb_post.models import Post, Comment
from .fb_post_details_of_post import get_post_details_in_dictionary
from .fb_post_exception_methods import check_whether_post_id_exists


# Task 13
def get_post(post_id):
    check_whether_post_id_exists(post_id)
    comment_objects = Comment.objects.select_related('commented_by')
    comment_prefetch = Prefetch('comments', queryset=comment_objects)
    post = (Post.objects
            .filter(id=post_id)
            .select_related('posted_by')
            .prefetch_related(comment_prefetch,
                              'reactions',
                              'comments__reactions')
            .get(id=post_id))
    post_dict = get_post_details_in_dictionary(post)
    return post_dict
