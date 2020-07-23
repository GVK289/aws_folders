from django.db.models import Count
from fb_post.models import Post, Reaction
from .fb_post_exception_methods import check_whether_post_id_exists


def get_reaction_metrics(post_id):
    check_whether_post_id_exists(post_id)
    reaction_metrics_in_dict = dict(Reaction.objects
                                    .filter(post=Post(post_id))
                                    .values_list('reaction')
                                    .annotate(Count('id')))
    return reaction_metrics_in_dict
