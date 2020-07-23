from django.db.models import Count
from fb_post.models import Reaction


def get_total_reaction_count():
    dict_of_count_reactions = Reaction.objects.aggregate(count=Count(
        'reaction'))
    return dict_of_count_reactions
