from fb_post.constants import DatetimeFormat
from .user_info import dict_of_user_info


def get_post_details_in_dictionary(post_object):
    post_dic = {
        "post_id": post_object.id,
        "posted_by": dict_of_user_info(post_object.posted_by),
        "posted_at": post_object.posted_at.strftime(DatetimeFormat),
        "post_content": post_object.content,
        "reactions": get_post_reactions_in_dict(post_object)
    }
    comment_list = get_post_comment_list(post_object.comments.all())
    post_dic['comments'] = comment_list
    post_dic['comments_count'] = len(comment_list)
    return post_dic


def get_comment_from_comment_object(comment_obj):
    commented_at = comment_obj.commented_at.strftime(DatetimeFormat)
    comment_dict = {
        'comment_id': comment_obj.id,
        'commenter': dict_of_user_info(comment_obj.commented_by),
        'commented_at': commented_at,
        'comment_content': comment_obj.content,
        'reactions': get_post_reactions_in_dict(comment_obj)
    }
    return comment_dict


def get_post_comment_list(comments):
    comment_list = []
    for comment_obj in comments:
        comment_parent_id_is_not_none = not comment_obj.parent_comment_id
        if comment_parent_id_is_not_none:
            comment_dict = get_comment_and_reply_objects(comment_obj,
                                                         comments)
            comment_list.append(comment_dict)
    return comment_list


def get_comment_and_reply_objects(comment_obj, comments):
    comment_dict = get_comment_from_comment_object(comment_obj)
    reply_list = []
    for reply_obj in comments:
        reply_parent_id_and_comment_id_same = (reply_obj.parent_comment_id ==
                                               comment_obj.id)
        if reply_parent_id_and_comment_id_same:
            reply_dict = get_comment_from_comment_object(reply_obj)
            reply_list.append(reply_dict)
    comment_dict['replies_count'] = len(reply_list)
    comment_dict['replies'] = reply_list
    return comment_dict


def get_post_reactions_in_dict(obj):
    reactions_dict = {"count": 0, "type": []}
    for reaction_obj in obj.reactions.all():
        reactions_dict['count'] += 1
        reaction_not_in_reactions_dict = (reaction_obj.reaction not
                                          in reactions_dict['type'])
        if reaction_not_in_reactions_dict:
            reactions_dict['type'].append(reaction_obj.reaction)
    return reactions_dict
