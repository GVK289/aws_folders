"""
Created on 14/05/20

@author: revanth
"""
from abc import abstractmethod, ABC


class EmployeeInterface(ABC):

    @abstractmethod
    def get_total_salary(self) -> int:
        pass
