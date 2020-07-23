from fb_post_clean_arch.presenters.presenter_implementation \
    import PresenterInterface
from fb_post_clean_arch.storages.storage_implementation \
    import StorageInterface


class CreatePostInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_post(self, user_id: int,
                    post_content: str,
                    presenter: PresenterInterface):
        post_id = self.storage.create_post(
            user_id=user_id,
            post_content=post_content
        )
        return presenter.get_create_post_response(post_id=post_id)
