from typing import List

from app.schemas.employees_validation import Employee


class EmployeesCrud:
    def __init__(self):
        self.collection = None

    async def read_employees(self, feature: str, value: str, option: str = None) -> List[Employee]:

        # TODO: В случае пагинации тут бы ограничивалось количество запрашиваемых документов
        # TODO: Еще можно добавить сортировку, получая дополнительный параметр на вход.

        if feature == "salary" or feature == "age":
            value = int(value)
        if option:
            cursor = self.collection.find({feature: {f"${option}": value}})
        else:
            cursor = self.collection.find({feature: value})
        return [employee async for employee in cursor]


employees_crud = EmployeesCrud()
