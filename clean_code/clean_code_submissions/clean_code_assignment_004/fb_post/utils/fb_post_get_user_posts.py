from django.db.models import Prefetch
from fb_post.models import Post, Comment
from .fb_post_details_of_post import get_post_details_in_dictionary
from .fb_post_exception_methods import check_whether_user_id_exists


def get_user_posts(user_id):
    check_whether_user_id_exists(user_id)
    comment_objects = Comment.objects.select_related('commented_by')
    comment_prefetch = Prefetch('comments', queryset=comment_objects)
    comments_reactions = 'comments__reactions'
    post_objects = (Post.objects
                    .filter(posted_by_id=user_id)
                    .select_related('posted_by')
                    .prefetch_related(comment_prefetch,
                                      'reactions',
                                      comments_reactions))
    user_posts_list = [get_post_details_in_dictionary(post_obj)
                       for post_obj in post_objects]
    return user_posts_list
