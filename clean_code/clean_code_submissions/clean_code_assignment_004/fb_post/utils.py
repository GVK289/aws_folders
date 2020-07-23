from .models import User, Post, Comment, Reaction
from datetime import datetime
from django.db.models import Avg, Max, FloatField, Count, Q, Min, Prefetch, F
from django.forms import model_to_dict
from collections import defaultdict
from .exceptions import *

def check_whether_user_id_exists(user_id):
    user_object = User.objects.filter(id=user_id)
    if not user_object:
        raise InvalidUserException
    else:
        return user_object[0]

def check_whether_post_id_exists(post_id):
    post_object = Post.objects.filter(id=post_id)
    if not post_object:
        raise InvalidPostException
    else:
        return post_object[0]

def check_whether_comment_id_exists(comment_id):
    comment_object = Comment.objects.filter(id=comment_id)
    if not comment_object:
        raise InvalidCommentException
    else:
        return comment_object[0]

def check_whether_reaction_type_exists(reaction_type):
    reactions = ['WOW', 'LIT', 'LOVE', 'HAHA', 'THUMBS-UP', 'THUMBS-DOWN',
                 'ANGRY', 'SAD']
    if reaction_type not in reactions:
        raise InvalidReactionTypeException

# Task 02
def create_post(user_id, post_content):
    user_object = check_whether_user_id_exists(user_id)
    if not post_content:
        raise InvalidPostContent
    return (Post.objects.create(posted_by_id=user_id,
                                content=post_content).id)

# Task 03
def create_comment(user_id, post_id, comment_content):
    user_object = check_whether_user_id_exists(user_id)
    post_object = check_whether_post_id_exists(post_id)
    if not comment_content:
        raise InvalidCommentContent
    return (Comment.objects.create(commented_by_id=user_id,
                                   post=post_object,
                                   content=comment_content).id)

# Task 04
def reply_to_comment(user_id, comment_id, reply_content):
    user_object = check_whether_user_id_exists(user_id)
    comment_object = check_whether_comment_id_exists(comment_id)
    if not reply_content:
        raise InvalidReplyContent
    if comment_object.parent_comment_id != None:
        comment_id = comment_object.parent_comment_id
    return (Comment.objects.create(commented_by_id=user_id,
                                   post_id=comment_object.post_id,
                                   parent_comment_id=comment_id,
                                   content=reply_content).id)

# Task 05
def react_to_post(user_id, post_id, reaction_type):
    user_object = check_whether_user_id_exists(user_id)
    post_object = check_whether_post_id_exists(post_id)
    check_whether_reaction_type_exists(reaction_type)
    reaction_object = Reaction.objects.filter(reacted_by_id=user_id,
                                              post_id=post_id)
    if reaction_object:
        if reaction_type in reaction_object[0].reaction:
            reaction_object[0].delete()
        else:
            reaction_object.update(reaction=reaction_type)
    else:
        Reaction.objects.create(reacted_by_id=user_id, post_id=post_id,
                                reaction=reaction_type)

# Task 06
def react_to_comment(user_id, comment_id, reaction_type):
    user_object = check_whether_user_id_exists(user_id)
    comment_object = check_whether_comment_id_exists(comment_id)
    check_whether_reaction_type_exists(reaction_type)
    reaction_object = Reaction.objects.filter(reacted_by_id=user_id,
                                              comment_id=comment_id)
    if reaction_object:
        if reaction_type in reaction_object[0].reaction:
            reaction_object[0].delete()
        else:
            reaction_object[0].reaction = reaction_type
            reaction_object[0].save()
    else:
        Reaction.objects.create(reacted_by_id=user_id, comment_id=comment_id,
                                reaction=reaction_type)

# Task 07
def get_total_reaction_count():
    return Reaction.objects.aggregate(count=Count('reaction'))

# Task 08
def get_reaction_metrics(post_id):
    post_object = check_whether_post_id_exists(post_id)
    reaction_metrics = dict(Reaction.objects.filter(post=Post(post_id))
                            .values_list('reaction')
                            .annotate(Count('id')))
    return reaction_metrics

# Task 09
def delete_post(user_id, post_id):
    user_object = check_whether_user_id_exists(user_id)
    post_object = check_whether_post_id_exists(post_id)
    if post_object.posted_by_id == user_id:
        post_object.delete()
    else:
        raise UserCannotDeletePostException

# Task 10
def get_posts_with_more_positive_reactions():
    Positive_reactions = ['THUMBS-UP', 'LIT', 'LOVE', 'HAHA', 'WOW']
    Negative_reactions = ['SAD', 'ANGRY', 'THUMBS-DOWN']
    no_of_positive_reactions = Count('reaction',
                                     filter=Q(reaction__in=Positive_reactions))
    no_of_negative_reactions = Count('reaction',
                                     filter=Q(reaction__in=Negative_reactions))
    posts_with_more_positive_reactions = list(Reaction.objects.annotate(
        positive_count=no_of_positive_reactions,
        negative_count=no_of_negative_reactions)
                                              .filter(positive_count__gt=
                                                      F('negative_count'))
                                              .values_list('post_id',
                                                           flat=True)
                                              .distinct())
    return posts_with_more_positive_reactions

# Task 11
def get_posts_reacted_by_user(user_id):
    user_object = check_whether_user_id_exists(user_id)
    posts_reacted_by_user = list(Reaction.objects.filter(
        reacted_by_id=user_id
        ).values_list('post_id', flat=True).distinct())
    return posts_reacted_by_user

# Task 12
def get_reactions_to_post(post_id):
    post_object = check_whether_post_id_exists(post_id)
    reactions_to_post = list(Reaction.objects.filter(post_id=post_id)
                             .annotate(user_id=F('reacted_by__id'),
                                       name=F('reacted_by__name'),
                                       profile_pic=F('reacted_by__profile_pic'))
                             .values('user_id', 'name', 'profile_pic',
                                     'reaction'))
    return reactions_to_post

# Task 13
def get_post(post_id, execute_with_query=True):
    if execute_with_query:
        post_object = check_whether_post_id_exists(post_id)
        post_object = Post.objects.filter(id=post_id
                                         ).select_related('posted_by'
                                                         ).prefetch_related(
                                                             Prefetch('comments',
                 queryset=Comment.objects.select_related('commented_by')),
                 'reactions', 'comments__reactions')[0]
    else:
        post_object = post_id
    post_dic = {}
    post_dic['post_id'] = post_object.id
    posted_by = {}
    posted_by['name'] = post_object.posted_by.name
    posted_by['user_id'] = post_object.posted_by.id
    posted_by['profile_pic'] = post_object.posted_by.profile_pic
    post_dic['posted_by'] = posted_by
    posted_at = post_object.posted_at.strftime('%Y-%m-%d %H:%M:%S.%f')
    post_dic['posted_at'] = posted_at
    post_dic['post_content'] = post_object.content
    reactions_dict = {"count":0,"type":[]}
    for reaction_obj in post_object.reactions.all():
        reactions_dict['count'] +=  1
        if reaction_obj.reaction not in reactions_dict['type']:
            reactions_dict['type'].append(reaction_obj.reaction)
    post_dic['reactions'] = reactions_dict
    comment_list = []
    for comment_obj in post_object.comments.all():
        if not(comment_obj.parent_comment_id):
            comment_dict = get_comment_from_comment_object(comment_obj)
            reply_list = []
            for reply_obj in post_object.comments.all():
                if reply_obj.parent_comment_id == comment_obj.id:
                    reply_dict = get_comment_from_comment_object(reply_obj)
                    reply_list.append(reply_dict)
            comment_dict['replies_count'] = len(reply_list)
            comment_dict['replies'] = reply_list
            comment_list.append(comment_dict)
    post_dic['comments'] = comment_list
    post_dic['comments_count'] = len(comment_list)

    return post_dic

# Task 14
def get_user_posts(user_id):
    user_object = check_whether_user_id_exists(user_id)
    post_objects = Post.objects.filter(posted_by_id=user_id
                                       ).select_related('posted_by'
                                        ).prefetch_related( 
                                        Prefetch('comments',queryset= 
                        Comment.objects.select_related('commented_by')),
                        'reactions','comments__reactions')
    user_posts_list = []
    for post_obj in post_objects:
        post_dic = get_post(post_obj,execute_with_query = False)
        user_posts_list.append(post_dic)
    return user_posts_list

# Task 15
def get_replies_for_comment(comment_id):
    comment_object = check_whether_comment_id_exists(comment_id)
    replies_for_comment_list = []
    comment_objects = list(Comment.objects.select_related('commented_by'
        ).filter(parent_comment_id=comment_id))
    for objects in comment_objects:
        replies_for_comment = {}
        replies_for_comment['comment_id'] = objects.id
        commenter_dict = {}
        commenter_dict['user_id'] = objects.commented_by_id
        commenter_dict['name'] = objects.commented_by.name
        commenter_dict['profile_pic'] = objects.commented_by.profile_pic
        replies_for_comment['commenter'] = commenter_dict
        commented_at = objects.commented_at.strftime('%Y-%m-%d %H:%M:%S.%f')
        replies_for_comment['commented_at'] = commented_at
        replies_for_comment['comment_content'] = objects.content
        replies_for_comment_list.append(replies_for_comment)
    return replies_for_comment_list

def get_comment_from_comment_object(obj):
    comment_dict = {}
    comment_dict['comment_id'] = obj.id
    commenter_dict = {}
    commenter_dict['user_id'] = obj.commented_by_id
    commenter_dict['name'] = obj.commented_by.name
    commenter_dict['profile_pic'] = obj.commented_by.profile_pic
    comment_dict['commenter'] = commenter_dict
    commented_at = obj.commented_at.strftime('%Y-%m-%d %H:%M:%S.%f')
    comment_dict['commented_at'] = commented_at
    comment_dict['comment_content'] = obj.content
    reactions_dict = {"count":0,"type":[]}
    for reaction_obj in obj.reactions.all():
        reactions_dict['count'] +=  1
        if reaction_obj.reaction not in reactions_dict['type']:
            reactions_dict['type'].append(reaction_obj.reaction)
    comment_dict['reactions'] = reactions_dict
    return comment_dict
