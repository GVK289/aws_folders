from fb_post.models import Reaction
from .fb_post_exception_methods import (check_whether_user_id_exists,
                                        check_whether_comment_id_exists,
                                        check_whether_reaction_type_exists)
from .fb_post_react_to_post import undo_reaction, update_reaction


# Task 06
def react_to_comment(user_id, comment_id, reaction_type):
    check_whether_user_id_exists(user_id)
    check_whether_comment_id_exists(comment_id)
    check_whether_reaction_type_exists(reaction_type)
    try:
        reaction_object = Reaction.objects.get(reacted_by_id=user_id,
                                               comment_id=comment_id)
    except Reaction.DoesNotExist:
        Reaction.objects.create(reacted_by_id=user_id,
                                comment_id=comment_id,
                                reaction=reaction_type)
        return
    comment_reaction_is_same_as_reaction_type = (reaction_type ==
                                                 reaction_object.reaction)
    if comment_reaction_is_same_as_reaction_type:
        undo_reaction(reaction_object)
    else:
        update_reaction(reaction_object, reaction_type)
