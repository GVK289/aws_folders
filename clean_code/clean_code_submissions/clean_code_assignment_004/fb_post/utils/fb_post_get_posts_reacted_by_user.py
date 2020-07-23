from fb_post.models import Reaction
from .fb_post_exception_methods import check_whether_user_id_exists


# Task 11
def get_posts_reacted_by_user(user_id):
    check_whether_user_id_exists(user_id)
    list_of_posts_reacted_by_user = list(Reaction.objects
                                         .filter(reacted_by_id=user_id)
                                         .values_list('post_id', flat=True)
                                         .distinct())
    return list_of_posts_reacted_by_user
