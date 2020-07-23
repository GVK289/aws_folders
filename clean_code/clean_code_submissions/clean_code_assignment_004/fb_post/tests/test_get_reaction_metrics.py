import pytest
from fb_post.exceptions import InvalidPostException
from fb_post.constants import ReactionType
from fb_post.utils import get_reaction_metrics


pytestmark = pytest.mark.django_db


def test_get_reaction_metrics_when_post_id_is_invalid_raises_invalid_post_exception(reaction):
    # Arrange
    invalid_post_id = 100

    # Act
    with pytest.raises(InvalidPostException):
        assert get_reaction_metrics(invalid_post_id)


def test_get_reaction_metrics_if_post_has_reactions_returns_total_number_of_reactions_for_each_reaction_type_in_dictionary(reaction):
    # Arrange
    post_id = 1
    reaction_metrics_dict = {ReactionType.WOW.value: 1,
                             ReactionType.LIT.value: 1}

    # Act
    each_reaction_type_metrics_dict = get_reaction_metrics(post_id)

    # Assert
    assert reaction_metrics_dict == each_reaction_type_metrics_dict


def test_get_reaction_metrics_if_post_has_no_reactions_returns_empty_dictionary(reaction):
    # Arrange
    post_id = 5
    reaction_metrics_dict = {}

    # Act
    each_reaction_type_metrics_dict = get_reaction_metrics(post_id)

    # Assert
    assert reaction_metrics_dict == each_reaction_type_metrics_dict
