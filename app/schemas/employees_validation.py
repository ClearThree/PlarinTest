from typing import List

from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: str
    job_title: str
    gender: str
    salary: int


class GetEmployeesResponse(BaseModel):
    __root__: List[Employee]
