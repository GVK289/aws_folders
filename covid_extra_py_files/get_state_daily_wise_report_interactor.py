# from covid_dashboard.interactors.storages.state_storage_interface \
#     import StateStorageInterface
# from covid_dashboard.interactors.presenters.presenter_interface \
#     import PresenterInterface
# from covid_dashboard.exceptions.exceptions \
#     import InvalidStateIdException


# class GetStateStorageDailyWiseReportInteractor:

#     def __init__(self,
#                  state_storage: StateStorageInterface,
#                  presenter: PresenterInterface):
#         self.state_storage = state_storage
#         self.presenter = presenter

#     def get_state_daily_wise_report(self,
#                                          state_id: int):
#         try:
#             self.state_storage.validate_state_id(state_id)
#         except InvalidStateIdException:
#             self.presenter.raise_state_exception_if_state_id_is_invalid()
#             return

#         daily_state_wise_report_dto = self. \
#             state_storage.get_state_daily_wise_report(
#                 state_id=state_id)

#         return self.presenter. \
#             get_response_for_get_state_daily_wise_report(
#                 daily_state_wise_report_dto=
#                 daily_state_wise_report_dto)
