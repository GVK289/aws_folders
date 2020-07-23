from fb_post_clean_arch.exceptions.custom_exceptions import InvalidPostId
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class GetPostReactionsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_post_reactions(self,
                           post_id: int,
                           presenter: PresenterInterface):
        try:
            self.storage.validate_post_id(post_id=post_id)
        except InvalidPostId:
            return presenter.raise_exception_for_invalid_post()
        post_reaction_dtos = self.storage.get_post_reaction_dtos(
            post_id=post_id)
        return presenter.get_response_for_get_post_reactions(
            post_reaction_dtos=post_reaction_dtos)
