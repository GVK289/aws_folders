from fb_post.models import User


def dict_of_user_info(user):
    user_dict = {
        'user_id': user.id,
        'name': user.name,
        'profile_pic': user.profile_pic
    }
    return user_dict
