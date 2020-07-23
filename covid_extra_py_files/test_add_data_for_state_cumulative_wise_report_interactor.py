# import pytest
# from datetime import date
# from unittest.mock import create_autospec
# from django_swagger_utils.drf_server.exceptions import NotFound

# from covid_dashboard.interactors. \
#     add_data_for_state_cumulative_wise_report_interactor import \
#     AddDataForStateCumulativeWiseReportInteractor
# from covid_dashboard.interactors.storages.state_storage_interface \
#     import StateStorageInterface
# from covid_dashboard.interactors.presenters.presenter_interface \
#     import PresenterInterface

# from covid_dashboard.interactors.storages.dtos \
#     import CumulativeStateWiseReportDto, CumulativeStateReportDto

# from covid_dashboard.exceptions.exceptions import InvalidStateIdException


# def test_with_invalid_state_id_raises_exceptions():
#     # Arrange
#     state_id = "gv"
#     total_confirmed_cases = 100
#     total_active_cases = 90
#     total_deaths = 6
#     total_recovered_cases = 4

#     storage = create_autospec(StateStorageInterface)
#     presenter = create_autospec(PresenterInterface)

#     storage.validate_state_id.side_effect = InvalidStateIdException
#     presenter.raise_state_exception_if_state_id_is_invalid. \
#         side_effect = NotFound

#     interactor = AddDataForStateCumulativeWiseReportInteractor(
#         state_storage=storage,
#         presenter=presenter)

#     # Act
#     with pytest.raises(NotFound):
#         interactor.add_data_for_state_cumulative_wise_report(
#             state_id=state_id,
#             total_confirmed_cases=total_confirmed_cases,
#             total_active_cases=total_active_cases,
#             total_deaths=total_deaths,
#             total_recovered_cases=total_recovered_cases)


# def test_add_data_for_state_cumulative_report_with_valid_details(
#         state_dtos,
#         cumulative_state_wise_report_dtos,
#         get_deatils_for_cumulative_state_wise_report):
#     # Arrange
#     state_id = 1
#     total_confirmed_cases = 100
#     total_active_cases = 90
#     total_deaths = 6
#     total_recovered_cases = 4
#     select_date_for_details = date.today()
#     state_name = "AndharaPradesh"
    
#     expected_details_of_cumulative_state_wise_report_dict = \
#         get_deatils_for_cumulative_state_wise_report

#     storage = create_autospec(StateStorageInterface)
#     presenter = create_autospec(PresenterInterface)

#     interactor = AddDataForStateCumulativeWiseReportInteractor(
#         state_storage=storage,
#         presenter=presenter)

#     cumulative_state_report = CumulativeStateReportDto(
#         total_confirmed_cases=total_confirmed_cases,
#         total_active_cases=total_active_cases,
#         total_deaths=total_deaths,
#         total_recovered_cases=total_recovered_cases
#     )

#     cumulative_state_wise_report_dto = CumulativeStateWiseReportDto(
#         date=select_date_for_details,
#         state_name=state_name,
#         cumulative_state_report=cumulative_state_report
#     )

#     storage.add_data_for_state_cumulative_wise_report. \
#         return_value = cumulative_state_wise_report_dto
#     presenter.get_response_add_data_for_state_cumulative_wise_report. \
#         return_value = expected_details_of_cumulative_state_wise_report_dict

#     # Act
#     details_of_cumulative_state_wise_report_dict = interactor. \
#         add_data_for_state_cumulative_wise_report(
#             state_id=state_id,
#             total_confirmed_cases=total_confirmed_cases,
#             total_active_cases=total_active_cases,
#             total_deaths=total_deaths,
#             total_recovered_cases=total_recovered_cases)

#     # Assert
#     assert details_of_cumulative_state_wise_report_dict == \
#         expected_details_of_cumulative_state_wise_report_dict
#     storage.validate_state_id.assert_called_once_with(state_id=state_id)
#     presenter.get_response_add_data_for_state_cumulative_wise_report. \
#         assert_called_once_with(
#             cumulative_state_wise_report_dto=cumulative_state_wise_report_dto)
