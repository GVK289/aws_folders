import pytest
from fb_post.utils import get_total_reaction_count


pytestmark = pytest.mark.django_db


def test_get_total_reaction_count_if_user_reactions_are_available_returns_total_reactions_count_in_dictionary(reaction, reaction_to_comments):
    # Arrange
    total_reaction_count_dict = {'count': 11}

    # Act
    reaction_count_dict = get_total_reaction_count()

    # Assert
    assert total_reaction_count_dict == reaction_count_dict


def test_get_total_reaction_count_if_user_reactions_are_unavailable_returns_total_reactions_count_with_zero_value_in_dictionary():
    # Arrange
    total_reaction_count_dict = {'count': 0}

    # Act
    reaction_count_dict = get_total_reaction_count()

    # Assert
    assert total_reaction_count_dict == reaction_count_dict
