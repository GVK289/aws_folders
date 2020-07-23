"""
Created on 14/05/20

@author: revanth
"""
from typing import List
from source_code_dependency_inversion_example.calculate_pay.\
    employee_interface import EmployeeInterface


class PayoutCalculator:

    @classmethod
    def calculate_payout(cls, employees: List[EmployeeInterface]):
        total_payout = 0
        for each_employee in employees:
            total_payout += each_employee.get_total_salary()

        print('Total payout: {}'.format(total_payout))
