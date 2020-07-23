# from covid_dashboard.interactors.storages.state_storage_interface \
#     import StateStorageInterface
# from covid_dashboard.interactors.presenters.presenter_interface \
#     import PresenterInterface
# from covid_dashboard.exceptions.exceptions \
#     import InvalidStateIdException


# class AddDataForStateCumulativeWiseReportInteractor:

#     def __init__(self,
#                  state_storage: StateStorageInterface,
#                  presenter: PresenterInterface):
#         self.state_storage = state_storage
#         self.presenter = presenter

#     def add_data_for_state_cumulative_wise_report(
#             self,
#             state_id: int,
#             total_confirmed_cases: int,
#             total_active_cases: int,
#             total_deaths: int,
#             total_recovered_cases: int
#             ):
#         try:
#             self.state_storage.validate_state_id(state_id)
#         except InvalidStateIdException:
#             self.presenter.raise_state_exception_if_state_id_is_invalid()
#             return

#         cumulative_state_wise_report_dto = self.state_storage. \
#             add_data_for_state_cumulative_wise_report(
#                 state_id=state_id,
#                 total_confirmed_cases=total_confirmed_cases,
#                 total_active_cases=total_active_cases,
#                 total_deaths=total_deaths,
#                 total_recovered_cases=total_recovered_cases)
#         return self.presenter. \
#             get_response_add_data_for_state_cumulative_wise_report(
#                 cumulative_state_wise_report_dto=
#                 cumulative_state_wise_report_dto)
