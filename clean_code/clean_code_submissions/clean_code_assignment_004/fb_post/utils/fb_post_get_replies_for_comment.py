from fb_post.constants import DatetimeFormat
from fb_post.models import Comment
from .fb_post_exception_methods import check_whether_comment_id_exists
from .user_info import dict_of_user_info


# Task 15
def get_replies_for_comment(comment_id):
    check_whether_comment_id_exists(comment_id)
    replies_list = list(Comment.objects
                        .filter(parent_comment_id=comment_id)
                        .select_related('commented_by'))
    list_of_replies_details_dict = [get_reply_details(reply)
                                    for reply in replies_list]
    return list_of_replies_details_dict


def get_reply_details(reply_obj):
    commented_at = reply_obj.commented_at.strftime(DatetimeFormat)
    reply_comment_dict = {
        'comment_id': reply_obj.id,
        'commenter': dict_of_user_info(reply_obj.commented_by),
        'commented_at': commented_at,
        'comment_content': reply_obj.content,
    }
    return reply_comment_dict
