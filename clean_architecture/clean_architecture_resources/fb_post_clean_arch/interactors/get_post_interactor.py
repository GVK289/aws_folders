from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class GetPostInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_post(self,
                 post_id: int,
                 presenter: PresenterInterface):
        try:
            self.storage.validate_post_id(
                post_id=post_id
            )
        except InvalidPostId:
            return presenter.raise_exception_for_invalid_post()

        post_complete_details_dto = \
            self.storage.get_post_details_dto(post_id=post_id)
        post_details_dict = presenter.get_response_for_get_post_details(
            get_post_dto=post_complete_details_dto)
        return post_details_dict
