class BusinessDeveloper:

    def __init__(self, name: str, age: int, base_salary: int):
        self.name = name
        self.age = age
        self.base_salary = base_salary

    def _get_business_developer_bonus(self):
        return 9000

    def get_total_salary(self) -> int:
        total_salary = self.base_salary + self._get_business_developer_bonus()
        print('{} - Business Developer: {}'.format(self.name, total_salary))
        return total_salary
