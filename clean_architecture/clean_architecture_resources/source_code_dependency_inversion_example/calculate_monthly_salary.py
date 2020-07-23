"""
Created on 14/05/20

@author: revanth
"""


def calculate_monthly_salary():
    from source_code_dependency_inversion_example.employees.developer \
        import Developer
    from source_code_dependency_inversion_example.employees.designer \
        import Designer
    from source_code_dependency_inversion_example.employees.business_developer \
        import BusinessDeveloper
    from source_code_dependency_inversion_example.calculate_pay.\
        payout_calculator import PayoutCalculator

    developer_1 = Developer('Revanth', 25, 20000)
    developer_2 = Developer('Vedavidh', 27, 10000)
    designer_1 = Designer('Jaya Kiran', 29, 50000)
    designer_2 = Designer('Prudhvi', 29, 60000)
    business_developer1 = BusinessDeveloper('Vinay', 22, 30000)

    all_employees = [
        developer_1,
        developer_2,
        designer_1,
        designer_2,
        business_developer1
    ]
    PayoutCalculator.calculate_payout(all_employees)


if __name__ == '__main__':
    calculate_monthly_salary()
