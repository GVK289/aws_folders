import pytest
from fb_post.exceptions import InvalidUserException, InvalidCommentException
from fb_post.exceptions import InvalidReactionTypeException
from fb_post.constants import ReactionType
from fb_post.models import Reaction
from fb_post.utils import react_to_comment


pytestmark = pytest.mark.django_db


def test_react_to_comment_when_user_id_is_invalid_raises_invalid_user_exception(comment):
    # Arrange
    invalid_user_id = 100
    comment_id = 3
    reaction_type = ReactionType.HAHA.value

    # Act
    with pytest.raises(InvalidUserException):
        assert react_to_comment(invalid_user_id, comment_id, reaction_type)


def test_react_to_comment_when_comment_id_is_invalid_raises_invalid_comment_exception(comment):
    # Arrange
    user_id = 1
    invalid_comment_id = 100
    reaction_type = ReactionType.HAHA.value

    # Act
    with pytest.raises(InvalidCommentException):
        assert react_to_comment(user_id, invalid_comment_id, reaction_type)


def test_react_to_comment_when_reaction_type_is_invalid_raises_invalid_reaction_type_exception(comment):
    # Arrange
    user_id = 1
    comment_id = 1
    invalid_reaction_type = 'reaction1'

    # Act
    with pytest.raises(InvalidReactionTypeException):
        assert react_to_comment(user_id, comment_id, invalid_reaction_type)


def test_react_to_comment_create_reaction_if_user_is_reacting_to_post_for_first_time_with_valid_details_creates_reaction_object(comment, reaction):
    # Arrange
    user_id = 1
    comment_id = 5
    reaction_type = ReactionType.HAHA.value

    # Act
    react_to_comment(user_id, comment_id, reaction_type)

    # Asset
    assert Reaction.objects.filter(comment_id=comment_id).exists()
    assert Reaction.objects.filter(comment_id=comment_id,
                                   reacted_by_id=user_id).exists()
    assert Reaction.objects.filter(reaction=reaction_type).exists()


def test_react_to_comment_when_user_already_reacted_to_post_and_user_reaction_type_is_same_as_given_reaction_type_then_delete_the_existing_reaction_of_user(reaction_to_comments):
    # Arrange
    user_id = 2
    comment_id = 1
    reaction_type = ReactionType.LIT.value
    # Act
    react_to_comment(user_id, comment_id, reaction_type)

    # Asset
    with pytest.raises(Reaction.DoesNotExist):
        assert Reaction.objects.get(comment_id=comment_id,
                                    reacted_by_id=user_id,
                                    reaction=reaction_type)


def test_react_to_comment_when_user_already_reacted_to_post_and_user_reaction_type_is_different_from_given_reaction_type_then_update_the_existing_reaction_of_user_with_latest_date_and_time(reaction_to_comments):
    # Arrange
    user_id = 2
    comment_id = 1
    old_reaction_type = ReactionType.LIT.value
    reaction_type = ReactionType.SAD.value
    old_reaction_obj = Reaction.objects.get(comment_id=comment_id,
                                            reacted_by_id=user_id,
                                            reaction=old_reaction_type)

    # Act
    react_to_comment(user_id, comment_id, reaction_type)

    # Asset
    new_reaction_object = Reaction.objects.get(comment_id=comment_id,
                                               reacted_by_id=user_id,
                                               reaction=reaction_type)
    assert old_reaction_obj.comment_id == new_reaction_object.comment_id
    assert old_reaction_obj.reacted_by_id == new_reaction_object.reacted_by_id
    assert not old_reaction_obj.reaction == new_reaction_object.reaction
    assert new_reaction_object.reaction == reaction_type
