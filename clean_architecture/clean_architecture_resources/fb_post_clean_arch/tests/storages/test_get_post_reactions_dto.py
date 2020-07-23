import pytest

from fb_post_clean_arch.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_post_reaction_dtos_given_post_id_returns_reactions_dto(
        create_users,
        create_post,
        create_post_reactions,
        user_dtos,
        post_reaction_dtos):

    post_id = 1
    user_dtos = user_dtos
    reactions_dtos = post_reaction_dtos
    sql_storage = StorageImplementation()

    post_reaction_dtos = sql_storage.get_post_reaction_dtos(post_id=post_id)

    assert user_dtos == post_reaction_dtos.user_dtos
    assert reactions_dtos == post_reaction_dtos.reaction_dtos



