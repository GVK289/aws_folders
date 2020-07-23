from django.test import TestCase

# Create your tests here.
from fb_post.utils import *
import pytest
from freezegun import freeze_time
import datetime

pytestmark = pytest.mark.django_db

@pytest.fixture
def user():
    User.objects.create(name = 'Vinay', profile_pic = 'gvk@gmail.com')
    
@pytest.fixture
def post(user):
    user = User.objects.get(name)
    Post.objects.create(content = 'post1', )

    
" Task 02 "

def test_create_post_when_user_is_inavlid_raises_inavlid_user_exception(user):
    # Arrange
    invalid_user_id = 2
    post_content = 'post1'
    
    # Act
    with pytest.raises(InvalidUserException) as e:  # Asserting the exception
        assert create_post(invalid_user_id, post_content)
        
def test_create_post_when_post_content_is_inavlid_raises_inavlid_post_content_exception(user):
    # Arrange
    valid_user_id = User.objects.get(name = 'Vinay').id
    post_content = ''
    
    # Act
    with pytest.raises(InvalidPostContent) as e:  # Asserting the exception
        assert create_post(valid_user_id, post_content)

@freeze_time("2012-01-14")
def test_create_post_when_valid_user_id_and_post_content_are_given_returns_post_id(user):
    # Arrange
    user_id = User.objects.get(name = 'Vinay').id
    
    # Act
    post_id = create_post(user_id,'post1')
    
    # Assert
    post_object = Post.objects.get(id = post_id)
    assert post_object.posted_by_id == user_id
    assert post_object.content == 'post1'
    assert post_object.posted_at.replace(tzinfo = None) == datetime.datetime.now()
    

" Task 03 "

"""
def test_create_comment_when_user_id_is_inavlid_raises_inavlid_user_exception(user, post):
    # Arrange
    invalid_user_id = 2
    post_id = Post.objects.get(name = 'post1')
    
    # Act
    with pytest.raises(InvalidUserException) as e:  # Asserting the exception
        assert create_comment(user_id, post_id, comment_content)
    
    
    

    
def test_create_comment_when_post_id_is_inavlid_raises_inavlid_post_exception(user_id, post_id, comment_content):
    
    
    
    
def test_create_comment_when_comment_content_is_inavlid_raises_inavlid_comment_content_exception(user_id, post_id, comment_content):
def test_create_post_when_valid_user_id_and_post_content_are_given_returns_post_id(user_id, post_id, comment_content):

"""













"""""
# task 1
test_user_construction_object_when_invalid_raises_exception
test_post_construction_object_when_invalid_raises_exception
test_comment_construction_object_when_invalid_raises_exception
test_reaction_construction_object_when_invalid_raises_exception


# task 2
test_create_post_when_user_is_inavlid_raises_inavlid_user_exception
test_create_post_when_post_content_is_inavlid_raises_inavlid_post_content_exception
test_create_post_when_valid_user_id_and_post_content_are_given_returns_post_id


# task 3
test_create_comment_when_user_id_is_inavlid_raises_inavlid_user_exception
test_create_comment_when_post_id_is_inavlid_raises_inavlid_post_exception
test_create_comment_when_comment_content_is_inavlid_raises_inavlid_comment_content_exception
test_create_post_when_valid_user_id_and_post_content_are_given_returns_post_id


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


# task 12

test_get_reactions_to_post_when_post_id_is_inavlid_raises_inavlid_post_exception
test_get_reactions_to_post_if_post_has_reactions_returns_list_of_dictionaries_of_user_details_of_post
test_get_reactions_to_post_if_post_has_no_reactions_returns_empty_list






"""""