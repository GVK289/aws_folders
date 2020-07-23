from fb_post.models import Reaction
from .fb_post_exception_methods import (check_whether_user_id_exists,
                                        check_whether_post_id_exists,
                                        check_whether_reaction_type_exists)


# Task 05
def react_to_post(user_id, post_id, reaction_type):
    check_whether_user_id_exists(user_id)
    check_whether_post_id_exists(post_id)
    check_whether_reaction_type_exists(reaction_type)
    try:
        reaction_object = Reaction.objects.get(reacted_by_id=user_id,
                                               post_id=post_id)
    except Reaction.DoesNotExist:
        Reaction.objects.create(reacted_by_id=user_id,
                                post_id=post_id,
                                reaction=reaction_type)
        return
    post_reaction_is_same_as_reaction_type = (reaction_type ==
                                              reaction_object.reaction)
    if post_reaction_is_same_as_reaction_type:
        undo_reaction(reaction_object)
    else:
        update_reaction(reaction_object, reaction_type)


def undo_reaction(reaction_object):
    reaction_object.delete()


def update_reaction(reaction_object, reaction_type):
    reaction_object.reaction = reaction_type
    reaction_object.save()
