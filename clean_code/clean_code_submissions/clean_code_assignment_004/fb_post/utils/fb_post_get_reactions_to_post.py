from django.db.models import F
from fb_post.models import Reaction
from .fb_post_exception_methods import check_whether_post_id_exists


# Task 12
def get_reactions_to_post(post_id):
    check_whether_post_id_exists(post_id)
    list_of_reactions_to_post = list(Reaction.objects
                                     .filter(post_id=post_id)
                                     .annotate(user_id=F('reacted_by__id'),
                                               name=F('reacted_by__name'),
                                               profile_pic=F(
                                                   'reacted_by__profile_pic'))
                                     .values('user_id', 'name', 'profile_pic',
                                             'reaction'))
    return list_of_reactions_to_post
