import pytest
from fb_post.exceptions import InvalidUserException, InvalidPostException
from fb_post.exceptions import InvalidReactionTypeException
from fb_post.constants import ReactionType
from fb_post.models import Reaction
from fb_post.utils import react_to_post


pytestmark = pytest.mark.django_db


pytestmark = pytest.mark.django_db


def test_react_to_post_when_user_id_is_invalid_raises_invalid_user_exception(reaction):
    # Arrange
    invalid_user_id = 100
    post_id = 3
    reaction_type = ReactionType.HAHA.value

    # Act
    with pytest.raises(InvalidUserException):
        assert react_to_post(invalid_user_id, post_id, reaction_type)


def test_react_to_post_when_post_id_is_invalid_raises_invalid_post_exception(reaction):
    # Arrange
    user_id = 1
    invalid_post_id = 100
    reaction_type = ReactionType.HAHA.value

    # Act
    with pytest.raises(InvalidPostException):
        assert react_to_post(user_id, invalid_post_id, reaction_type)


def test_react_to_post_when_reaction_type_is_invalid_raises_invalid_reaction_type_exception(reaction):
    # Arrange
    user_id = 1
    post_id = 4
    invalid_reaction_type = 'reaction1'

    # Act
    with pytest.raises(InvalidReactionTypeException):
        assert react_to_post(user_id, post_id, invalid_reaction_type)


def test_react_to_post_create_reaction_if_user_is_reacting_to_post_for_first_time_with_valid_details_creates_reaction_object(reaction):
    # Arrange
    user_id = 1
    post_id = 3
    reaction_type = ReactionType.HAHA.value

    # Act
    react_to_post(user_id, post_id, reaction_type)

    # Asset
    assert Reaction.objects.filter(post_id=post_id).exists()
    assert Reaction.objects.filter(post_id=post_id,
                                   reacted_by_id=user_id).exists()
    assert Reaction.objects.filter(reaction=reaction_type).exists()


def test_react_to_post_when_user_already_reacted_to_post_and_user_reaction_type_is_same_as_given_reaction_type_then_delete_the_existing_reaction_of_user(reaction):
    # Arrange
    user_id = 2
    post_id = 1
    reaction_type = ReactionType.WOW.value

    # Act
    react_to_post(user_id, post_id, reaction_type)

    # Asset
    with pytest.raises(Reaction.DoesNotExist):
        assert Reaction.objects.get(post_id=post_id, reacted_by_id=user_id,
                                    reaction=reaction_type)


def test_react_to_post_when_user_already_reacted_to_post_and_user_reaction_type_is_different_from_given_reaction_type_then_update_the_existing_reaction_of_user_with_latest_date_and_time(reaction):
    # Arrange
    user_id = 2
    post_id = 1
    old_reaction_type = ReactionType.WOW.value
    reaction_type = ReactionType.LIT.value

    # Act
    react_to_post(user_id, post_id, reaction_type)

    # Asset
    new_reaction_object = Reaction.objects.get(post_id=post_id,
                                               reacted_by_id=user_id,
                                               reaction=reaction_type)
    assert post_id == new_reaction_object.post_id
    assert user_id == new_reaction_object.reacted_by_id
    assert not old_reaction_type == new_reaction_object.reaction
    assert new_reaction_object.reaction == reaction_type
