import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.interactors.get_post_interactor import \
    GetPostInteractor
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface, PostCompleteDetailsDto


class TestGetPostInteractor:
    def test_given_invalid_post_id_raises_exception(self):
        post_id = 1
        storage = create_autospec(StorageInterface)
        interactor = GetPostInteractor(storage=storage)
        presenter = create_autospec(PresenterInterface)

        storage.validate_post_id.side_effect = InvalidPostId
        presenter.raise_exception_for_invalid_post.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_post(post_id=post_id,
                                presenter=presenter)

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.raise_exception_for_invalid_post.assert_called_once()

    def test_given_valid_post_id_returns_post_details(self,
                                                      post_dto,
                                                      user_dtos,
                                                      comment_dtos,
                                                      reaction_dtos,
                                                      get_post_response):
        post_id = 1
        post_dto = post_dto
        user_dtos = user_dtos
        comment_dtos = comment_dtos
        reaction_dtos = reaction_dtos
        expected_post_details_dict = get_post_response
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostInteractor(storage=storage)

        get_post_dto = PostCompleteDetailsDto(post_dto=post_dto,
                                              users_dto=user_dtos,
                                              comments_dto=comment_dtos,
                                              reactions_dto=reaction_dtos)

        storage.get_post_details_dto.return_value = get_post_dto

        presenter.get_response_for_get_post_details.return_value = \
            expected_post_details_dict

        post_details_dict = interactor.get_post(
            post_id=post_id,
            presenter=presenter)

        assert post_details_dict == expected_post_details_dict
        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.get_response_for_get_post_details.assert_called_once_with(
            get_post_dto=get_post_dto)
