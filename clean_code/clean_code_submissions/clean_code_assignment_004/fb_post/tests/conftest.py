import pytest
from freezegun import freeze_time
from fb_post.constants import ReactionType
from fb_post.models import User, Post, Comment, Reaction

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    user_list = [{'name': 'user1', 'profile_pic': 'user1_pic'},
                 {'name': 'user2', 'profile_pic': 'user2_pic'},
                 {'name': 'user3', 'profile_pic': 'user3_pic'},
                 {'name': 'user4', 'profile_pic': 'user4_pic'},
                 {'name': 'user5', 'profile_pic': 'user5_pic'}]
    User.objects.bulk_create([User(name=user_dict['name'],
                                   profile_pic=user_dict['profile_pic'])
                              for user_dict in user_list])


@pytest.fixture
@freeze_time("2012-09-10 00:00:00.00")
def post(user):
    post_list = [
        {'content': 'post1', 'posted_by_id': 1},
        {'content': 'post2', 'posted_by_id': 1},
        {'content': 'post3', 'posted_by_id': 2},
        {'content': 'post4', 'posted_by_id': 3},
        {'content': 'post5', 'posted_by_id': 4}]
    Post.objects.bulk_create([Post(content=post_dict['content'],
                                   posted_by_id=post_dict['posted_by_id'])
                              for post_dict in post_list])


@pytest.fixture
@freeze_time("2012-09-10 00:00:00.00")
def comment(post):
    comment_list = [
        {'content': 'comment1', 'post_id': 1, 'commented_by_id': 1},
        {'content': 'comment2', 'post_id': 2, 'commented_by_id': 1},
        {'content': 'comment1', 'post_id': 1, 'commented_by_id': 2},
        {'content': 'comment2', 'post_id': 1, 'commented_by_id': 3},
        {'content': 'comment3', 'post_id': 2, 'commented_by_id': 3},
        {'content': 'comment4', 'post_id': 3, 'commented_by_id': 4},]
    Comment.objects.bulk_create([Comment(content=comment_dict['content'],
                                         post_id=comment_dict['post_id'],
                                         commented_by_id=comment_dict[
                                             'commented_by_id'])
                                 for comment_dict in comment_list])


@pytest.fixture
@freeze_time("2012-09-10 00:00:00.00")
def reaction(post):
    reaction_list = [
        {'post_id': 1, 'reaction': ReactionType.WOW.value, 'reacted_by_id': 2},
        {'post_id': 1, 'reaction': ReactionType.LIT.value, 'reacted_by_id': 3},
        {'post_id': 2, 'reaction': ReactionType.SAD.value, 'reacted_by_id': 4},
        {'post_id': 3, 'reaction': ReactionType.LIT.value, 'reacted_by_id': 5},
        {'post_id': 3, 'reaction': ReactionType.LIT.value, 'reacted_by_id': 2}]
    Reaction.objects.bulk_create([Reaction(post_id=reaction_dict['post_id'],
                                           reacted_by_id=reaction_dict[
                                               'reacted_by_id'],
                                           reaction=reaction_dict['reaction'])
                                  for reaction_dict in reaction_list])


@pytest.fixture
@freeze_time("2012-09-10 00:00:00.00")
def reaction_to_comments(comment):
    reaction_list = [
        {'comment_id': 1, 'reaction': ReactionType.LIT.value,
         'reacted_by_id': 2},
        {'comment_id': 1, 'reaction': ReactionType.THUMBS_DOWN.value,
         'reacted_by_id': 3},
        {'comment_id': 2, 'reaction': ReactionType.SAD.value,
         'reacted_by_id': 4},
        {'comment_id': 3, 'reaction': ReactionType.ANGRY.value,
         'reacted_by_id': 5},
        {'comment_id': 1, 'reaction': ReactionType.THUMBS_DOWN.value,
         'reacted_by_id': 4},
        {'comment_id': 4, 'reaction': ReactionType.THUMBS_UP.value,
         'reacted_by_id': 1}]
    reaction_obj_list = [Reaction(comment_id=reaction_dict['comment_id'],
                                  reacted_by_id=reaction_dict['reacted_by_id'],
                                  reaction=reaction_dict['reaction'])
                         for reaction_dict in reaction_list]
    Reaction.objects.bulk_create(reaction_obj_list)


@pytest.fixture
@freeze_time("2012-09-10 00:00:00.00")
def reply(comment):
    reply_list = [
        {'content': 'reply_to_comment1 by 2', 'post_id': 1, 'comment_id': 1,
         'commented_by_id': 2},
        {'content': 'reply_to_comment2 by 3', 'post_id': 2, 'comment_id': 2,
         'commented_by_id': 3},
        {'content': 'reply_to_comment1 by 3', 'post_id': 3, 'comment_id': 6,
         'commented_by_id': 4},
        {'content': 'reply_to_comment4 by 1', 'post_id': 1, 'comment_id': 4,
         'commented_by_id': 1},]
    comment_obj_list = [Comment(content=comment_dict['content'],
                                post_id=comment_dict['post_id'],
                                parent_comment_id=comment_dict['comment_id'],
                                commented_by_id=comment_dict[
                                    'commented_by_id'])
                        for comment_dict in reply_list]
    Comment.objects.bulk_create(comment_obj_list)
