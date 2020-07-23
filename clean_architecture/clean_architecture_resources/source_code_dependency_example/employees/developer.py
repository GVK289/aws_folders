"""
Created on 14/05/20

@author: revanth
"""


class Developer:

    def __init__(self, name: str, age: int, base_salary: int):
        self.name = name
        self.age = age
        self.base_salary = base_salary

    def _get_developer_bonus(self):
        return 10000

    def get_total_salary(self):
        total_salary = self.base_salary + self._get_developer_bonus()
        print('{} - Developer: {}'.format(self.name, total_salary))
        return total_salary
