from django.db.models import Count, Q, F
from fb_post.models import Reaction
from fb_post.constants import ReactionType

# Task 10
def get_posts_with_more_positive_reactions():
    positive_reactions = [
        ReactionType.THUMBS_UP.value,
        ReactionType.LIT.value,
        ReactionType.LOVE.value,
        ReactionType.HAHA.value,
        ReactionType.WOW.value
        ]
    negative_reactions = [
        ReactionType.SAD.value,
        ReactionType.ANGRY.value,
        ReactionType.THUMBS_DOWN.value
        ]
    no_of_positive_reactions = Count('reaction',
                                     filter=Q(reaction__in=positive_reactions))
    no_of_negative_reactions = Count('reaction',
                                     filter=Q(reaction__in=negative_reactions))
    posts_with_more_positive_reactions_list = list(
        Reaction.objects
        .annotate(positive_count=no_of_positive_reactions,
                  negative_count=no_of_negative_reactions)
        .filter(positive_count__gt=F('negative_count'))
        .values_list('post_id',flat=True)
        .distinct())
    return posts_with_more_positive_reactions_list
