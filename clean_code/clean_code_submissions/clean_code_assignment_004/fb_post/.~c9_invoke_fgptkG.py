from django.test import TestCase

# Create your tests here.
from fb_post.utils import *
import pytest
from freezegun import freeze_time
import datetime

pytestmark = pytest.mark.django_db

@pytest.fixture
def user():
    user_list = [{'name':'user1', 'profile_pic':'user1_pic'},
    {'name':'user10', 'profile_pic':'user10_pic'},
    {'name':'user3', 'profile_pic':'user3_pic'},
    {'name':'user4', 'profile_pic':'user4_pic'},
    {'name':'user5', 'profile_pic':'user5_pic'}
        ]
    
    User.objects.bulk_create([User(name = user_dict['name'], profile_pic = user_dict['profile_pic']) for user_dict in user_list])
    
    
    
@pytest.fixture
def post(user):
    post_list = [{'content':'post1','posted_by_id':1},
        {'content':'post2','posted_by_id':1},
        {'content':'post3','posted_by_id':2},
        {'content':'post4','posted_by_id':3},
        {'content':'post5','posted_by_id':4}
        ]
    Post.objects.bulk_create([Post(content = post_dict['content'], posted_by_id = post_dict['posted_by_id']) for post_dict in post_list])

@pytest.fixture
def comment(user,post):
    comment_list = [{'content':'comment1','post_id':1,'commented_by_id':1},
        {'content':'comment2','post_id':2,'commented_by_id':1}, 
        {'content':'comment1','post_id':1,'commented_by_id':2},
        {'content':'comment2','post_id':1,'commented_by_id':3},
        {'content':'comment3','post_id':2,'commented_by_id':3},
        {'content':'comment4','post_id':3,'commented_by_id':4},
        ]
    Comment.objects.bulk_create([Comment(content = comment_dict['content'], post_id = comment_dict['post_id'], commented_by_id = comment_dict['commented_by_id']) for comment_dict in comment_list])
    
@pytest.fixture
def reaction():
    reaction_list = [{'post_id':1,'reaction':'WOW','reacted_by_id':2}, 
    {'post_id':1,'reaction':'LIT','reacted_by_id':3},
    {'post_id':2,'reaction':'SAD','reacted_by_id':4},
    {'post_id':3,'reaction':'ANGRY','reacted_by_id':5}
        ]
    
    Reaction.objects.bulk_create([Reaction(post_id = reaction_dict['post_id'], reacted_by_id = reaction_dict['reacted_by_id'], reaction = reaction_dict['reaction'] ) for reaction_dict in reaction_list])
    

    
" Task 02 "

def test_create_post_when_user_is_inavlid_raises_inavlid_user_exception(user):
    # Arrange
    invalid_user_id = 100
    post_content = 'post1'
    
    # Act
    with pytest.raises(InvalidUserException) as e:  # Asserting the exception
        assert create_post(invalid_user_id, post_content)
        
def test_create_post_when_post_content_is_inavlid_raises_inavlid_post_content_exception(user):
    # Arrange
    valid_user_id = User.objects.get(name = 'user1').id
    post_content = ''
    
    # Act
    with pytest.raises(InvalidPostContent) as e:  # Asserting the exception
        assert create_post(valid_user_id, post_content)

@freeze_time("2009-01-14")
def test_create_post_when_valid_user_id_and_post_content_are_given_returns_post_id(user):
    # Arrange
    user_id = User.objects.get(name = 'user1').id
    
    # Act
    post_id = create_post(user_id,'post1')
    
    # Assert
    post_object = Post.objects.get(id = post_id)
    assert post_object.posted_by_id == user_id
    assert post_object.content == 'post1'
    assert post_object.posted_at.replace(tzinfo = None) == datetime.datetime.now()
    

" Task 03 "


def test_create_comment_when_user_id_is_inavlid_raises_inavlid_user_exception(user, post):
    # Arrange
    invalid_user_id = 100
    post_id = Post.objects.get(content = 'post1').id
    comment_content = 'comment1'
    
    # Act
    with pytest.raises(InvalidUserException) as e:  # Asserting the exception
        assert create_comment(invalid_user_id, post_id, comment_content)
    
def test_create_comment_when_post_id_is_inavlid_raises_inavlid_post_exception(user, post):
    # Arrange
    user_id = User.objects.get(name = 'user1').id
    invalid_post_id = 100
    comment_content = 'comment1'
    
    # Act
    with pytest.raises(InvalidPostException) as e:  # Asserting the exception
        assert create_comment(user_id, invalid_post_id, comment_content)

def test_create_comment_when_comment_content_is_inavlid_raises_inavlid_comment_content_exception(user, post):
    # Arrange
    user_id = User.objects.get(name = 'user1').id
    post_id = Post.objects.get(content = 'post1').id
    invalid_comment_content = ''
    
    # Act
    with pytest.raises(InvalidCommentContent) as e:  # Asserting the exception
        assert create_comment(user_id, post_id, invalid_comment_content)

@freeze_time("100110-01-14")
def test_create_comment_when_valid_user_id_and_comment_content_are_given_returns_created_comment_id(user, post):
    # Arrange
    user_id = User.objects.get(name = 'user1').id
    post_id = Post.objects.get(content = 'post1').id
    comment_content = 'comment1'
    
    # Act
    create_comment(user_id, post_id, comment_content)
    
    # Assert
    comment_object = Comment.objects.get(commented_by_id = user_id)
    assert comment_object.commented_by_id == user_id
    assert comment_object.post_id == post_id
    assert comment_object.content == 'comment1'
    assert comment_object.commented_at.replace(tzinfo = None) == datetime.datetime.now()


" Task 04 "
def test_reply_to_comment_when_user_id_is_inavlid_raises_inavlid_user_exception(user,post,comment):
    # Arrange
    invalid_user_id = 100
    comment_id = Comment.objects.filter(content = 'comment1')[0].id
    reply_content = 'reply to comment1'
    
    # Act
    with pytest.raises(InvalidUserException) as e:  # Asserting the exception
        assert reply_to_comment(invalid_user_id, comment_id, reply_content)
        
def test_reply_to_comment_when_comment_id_is_inavlid_raises_inavlid_comment_exception(user,post,comment):
    # Arrange
    user_id = User.objects.get(name = 'user1').id
    invalid_comment_id = 100
    reply_content = 'reply to comment1'
    
    # Act
    with pytest.raises(InvalidCommentException) as e:  # Asserting the exception
        assert reply_to_comment(user_id, invalid_comment_id, reply_content)


def test_reply_to_comment_when_reply_content_is_inavlid_raises_inavlid_reply_content_exception(user,post,comment):
    # Arrange
    user_id = User.objects.get(name = 'user1').id
    comment_id = Comment.objects.filter(content = 'comment1')[0].id
    invalid_reply_content = ''
    
    # Act
    with pytest.raises(InvalidReplyContent) as e:  # Asserting the exception
        assert reply_to_comment(user_id, comment_id, invalid_reply_content)

@freeze_time("2009-01-16")
def test_reply_to_comment_if_comment_id_corresponds_to_reply_create_post_object_returns_created_comment_id(user,post,comment):
    # Arrange
    user_id = User.objects.get(name = 'user1').id
    comment_id = Comment.objects.filter(content = 'comment1')[1].id
    reply_content = 'reply to comment1'
    
    # Act
    new_comment_id = reply_to_comment(user_id, comment_id, reply_content)
    
    # Assert
    comment_object = Comment.objects.get(id = new_comment_id)
    assert comment_object.commented_by_id == user_id
    assert comment_object.content == 'reply to comment1'
    assert comment_object.parent_comment_id == comment_id
    assert comment_object.commented_at.replace(tzinfo = None) == datetime.datetime.now()




" Task 05 "

def test_react_to_post_when_user_id_is_inavlid_raises_inavlid_user_exception(user,post,reaction):
    # Arrange
    invalid_user_id = 100
    post_id = 3
    reaction_type = 'HAHA'
    
    # Act
    with pytest.raises(InvalidUserException) as e:  # Asserting the exception
        assert react_to_post(invalid_user_id, post_id, reaction_type)

def test_react_to_post_when_post_id_is_inavlid_raises_inavlid_post_exception(user,post,reaction):
    # Arrange
    user_id = 1
    invalid_post_id = 100
    reaction_type = 'HAHA'
    
    # Act
    with pytest.raises(InvalidPostException) as e:  # Asserting the exception
        assert react_to_post(user_id, invalid_post_id, reaction_type)

def test_react_to_post_when_reaction_type_is_invalid_raises_invalid_reaction_type_exception(user,post,reaction):
    # Arrange
    user_id = 1
    post_id = 4
    invalid_reaction_type = 'reaction1'
    
    # Act
    with pytest.raises(InvalidReactionTypeException) as e:  # Asserting the exception
        assert react_to_post(user_id, post_id, invalid_reaction_type)


def test_react_to_post_create_reaction_if_user_is_reacting_to_post_for_first_time_with_valid_details_creates_reaction_object(user,post,reaction):
    # Arrange
    user_id = 1
    post_id = 3
    reaction_type = 'HAHA'
    
    # Act
    react_to_post(user_id, post_id, reaction_type)
    
    # Asset
    assert Reaction.objects.filter(post_id = post_id).exists()
    assert Reaction.objects.filter(post_id = post_id, reacted_by_id = user_id).exists()
    assert Reaction.objects.filter(reaction = reaction_type).exists()
    

def test_react_to_post_when_user_already_reacted_to_post_and_user_reaction_type_is_same_as_given_reaction_type_then_delete_the_existing_reaction_of_user(user,post,reaction):
    # Arrange
    user_id = 2
    post_id = 1
    reaction_type = 'WOW'
    
    # Act
    react_to_post(user_id, post_id, reaction_type)
    
    # Asset
    reaction_object = Reaction.objects.filter(post_id = post_id, reacted_by_id = user_id, reaction = reaction_type)
    assert reaction_object.exists() is False


def test_react_to_post_when_user_already_reacted_to_post_and_user_reaction_type_is_different_from_given_reaction_type_then_update_the_existing_reaction_of_user_with_latest_date_and_time(user,post,reaction):
    # Arrange
    user_id = 2
    post_id = 1
    old_reaction_type = 'WOW'
    reaction_type = 'LIT'
    old_reaction_object = Reaction.objects.create(post_id = post_id,reacted_by_id = user_id, reaction = old_reaction_type)
    
    # Act
    react_to_post(user_id, post_id, reaction_type)
    
    # Asset
    new_reaction_object = Reaction.objects.create(post_id = post_id,reacted_by_id = user_id, reaction = reaction_type)
    assert old_reaction_object.post_id == new_reaction_object.post_id
    assert old_reaction_object.reacted_by_id == new_reaction_object.reacted_by_id
    assert not(old_reaction_object.reaction  == new_reaction_object.reaction)
    assert new_reaction_object.reaction == 'LIT'
    

" Task 06 "

def test_react_to_comment_when_user_id_is_inavlid_raises_inavlid_user_exception(user,post,reaction):
    # Arrange
    invalid_user_id = 100
    comment_id = 3
    reaction_type = 'HAHA'
    
    # Act
    with pytest.raises(InvalidUserException) as e:  # Asserting the exception
        assert react_to_comment(invalid_user_id, comment_id, reaction_type)

def test_react_to_comment_when_comment_id_is_inavlid_raises_inavlid_comment_exception(user,post,reaction):
    # Arrange
    user_id = 1
    invalid_comment_id = 100
    reaction_type = 'HAHA'
    
    # Act
    with pytest.raises(InvalidCommentException) as e:  # Asserting the exception
        assert react_to_comment(user_id, invalid_comment_id, reaction_type)

def test_react_to_comment_when_reaction_type_is_invalid_raises_invalid_reaction_type_exception(user,post,reaction):
    # Arrange
    user_id = 1
    comment_id = 5
    invalid_reaction_type = 'reaction1'
    
    # Act
    with pytest.raises(InvalidReactionTypeException) as e:  # Asserting the exception
        assert react_to_comment(user_id, comment_id, invalid_reaction_type)

"""
def test_react_to_comment_create_reaction_if_user_is_reacting_to_post_for_first_time_with_valid_details_creates_reaction_object(user,post,reaction):
    # Arrange
    user_id = 1
    comment_id = 5
    reaction_type = 'HAHA'
    
    # Act
    react_to_comment(user_id, comment_id, reaction_type)
    
    # Asset
    assert Reaction.objects.filter(comment_id = comment_id).exists()
    assert Reaction.objects.filter(comment_id = comment_id, reacted_by_id = user_id).exists()
    assert Reaction.objects.filter(reaction = reaction_type).exists()
    

def test_react_to_comment_when_user_already_reacted_to_post_and_user_reaction_type_is_same_as_given_reaction_type_then_delete_the_existing_reaction_of_user(user,post,reaction):
    # Arrange
    user_id = 1
    comment_id = 5
    reaction_type = 'HAHA'
    
    # Act
    react_to_comment(user_id, comment_id, reaction_type)
    
    # Asset
    reaction_object = Reaction.objects.filter(comment_id = comment_id, reacted_by_id = user_id, reaction = reaction_type)
    assert reaction_object.exists() is False


def test_react_to_comment_when_user_already_reacted_to_post_and_user_reaction_type_is_different_from_given_reaction_type_then_update_the_existing_reaction_of_user_with_latest_date_and_time(user,post,reaction):
    # Arrange
    user_id = 1
    comment_id = 5
    old_reaction_type = 'HAHA'
    reaction_type = 'LIT'
    old_reaction_object = Reaction.objects.create(comment_id = comment_id,reacted_by_id = user_id, reaction = old_reaction_type)
    
    # Act
    react_to_comment(user_id, comment_id, reaction_type)
    
    # Asset
    new_reaction_object = Reaction.objects.create(comment_id = comment_id,reacted_by_id = user_id, reaction = reaction_type)
    assert old_reaction_object.comment_id == new_reaction_object.comment_id
    assert old_reaction_object.reacted_by_id == new_reaction_object.reacted_by_id
    assert not(old_reaction_object.reaction  == new_reaction_object.reaction)
    assert new_reaction_object.reaction == 'LIT'
    

"""



"""    









"""






"""""
# task 1
test_user_construction_object_when_invalid_raises_exception
test_post_construction_object_when_invalid_raises_exception
test_comment_construction_object_when_invalid_raises_exception
test_reaction_construction_object_when_invalid_raises_exception


# task 10
test_create_post_when_user_is_inavlid_raises_inavlid_user_exception
test_create_post_when_post_content_is_inavlid_raises_inavlid_post_content_exception
test_create_post_when_valid_user_id_and_post_content_are_given_returns_post_id


# task 3
test_create_comment_when_user_id_is_inavlid_raises_inavlid_user_exception
test_create_comment_when_post_id_is_inavlid_raises_inavlid_post_exception
test_create_comment_when_comment_content_is_inavlid_raises_inavlid_comment_content_exception
test_create_comment_when_valid_user_id_and_comment_content_are_given_returns_created_comment_id


# task 4
test_reply_to_comment_when_user_id_is_inavlid_raises_inavlid_user_exception
test_reply_to_comment_when_comment_id_is_inavlid_raises_inavlid_comment_exception
test_reply_to_comment_when_reply_content_is_inavlid_raises_inavlid_reply_content_exception
test_reply_to_comment_if_comment_id_corresponds_to_reply_create_post_object_returns_created_comment_id


# task 5
test_react_to_post_when_user_id_is_inavlid_raises_inavlid_user_exception
test_react_to_post_when_post_id_is_inavlid_raises_inavlid_post_exception
test_react_to_post_when_reaction_type_is_invalid_raises_invalid_reaction_type_exception
test_react_to_post_create_reaction_if_user_is_reacting_to_post_for_first_time_with_valid_details_creates_reaction_object
test_react_to_post_when_user_already_reacted_to_post_and_user_reaction_type_is_same_as_given_reaction_type_then_delete_the_existing_reaction_of_user
test_react_to_post_when_user_already_reacted_to_post_and_user_reaction_type_is_different_from_given_reaction_type_then_update_the_existing_reaction_of_user_with_latest_date_and_time


# task 6
test_react_to_comment_when_user_id_is_inavlid_raises_inavlid_user_exception
test_react_to_comment_when_comment_id_is_inavlid_raises_inavlid_comment_exception
test_react_to_comment_when_reaction_type_is_invalid_raises_invalid_reaction_type_exception
test_react_to_comment_create_reaction_if_user_is_reacting_to_comment_for_first_time_with_valid_details_creates_reaction_object
test_react_to_comment_when_user_already_reacted_to_comment_and_user_reaction_type_is_same_as_given_reaction_type_then_delete_the_existing_reaction_of_user
test_react_to_comment_when_user_already_reacted_to_comment_and_user_reaction_type_is_different_from_given_reaction_type_then_update_the_existing_reaction_of_user_with_latest_date_and_time


# task 7
test_get_total_reaction_count_if_user_reactions_are_available_returns_total_reactions_count_in_dictionary
test_get_total_reaction_count_if_user_reactions_are_unavailable_returns_total_reactions_count_with_zero_value_in_dictionary


# task 8
test_get_reaction_metrics_when_post_id_is_inavlid_raises_inavlid_post_exception
test_get_reaction_metrics_if_post_has_reactions_returns_total_number_of_reactions_for_each_reaction_type_in_dictionary
test_get_reaction_metrics_if_post_has_no_reactions_returns_empty_dictionary


# task 9
test_delete_post_when_user_id_is_inavlid_raises_inavlid_user_exception
test_delete_post_when_post_id_is_inavlid_raises_inavlid_post_exception
test_delete_post_when_user_is_not_the_creator_of_post_raises_user_cannot_delete_post_exception
test_delete_post_when_user_is_the_creator_of_post_delete_the_post_object


# task 10
test_get_posts_with_more_positive_reactions_if_positive_reactions_of_post_greater_than_negative_reactions_of_post_returns_post_ids_of_posts_in_list
test_get_posts_with_more_positive_reactions_if_positive_reactions_of_post_not_greater_than_negative_reactions_of_post_returns_empty_list


# task 11
test_get_posts_reacted_by_user_when_user_id_is_inavlid_raises_inavlid_user_exception
test_get_posts_reacted_by_user_when_user_reacts_to_posts_returns_post_ids_of_user_reacted_posts_in_list
test_get_posts_reacted_by_user_when_user_does_not_react_to_any_posts_returns_empty_list


# task 110

test_get_reactions_to_post_when_post_id_is_inavlid_raises_inavlid_post_exception
test_get_reactions_to_post_if_post_has_reactions_returns_list_of_dictionaries_of_user_details_of_post
test_get_reactions_to_post_if_post_has_no_reactions_returns_empty_list






"""""