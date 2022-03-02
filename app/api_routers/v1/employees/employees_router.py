from logging import getLogger
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from app.crud.employees import employees_crud
from app.schemas.employees_validation import Employee, GetEmployeesResponse
from app.utils.dependencies import check_secret_token
from app.utils.logger import set_logging_parameters


LOGGER = set_logging_parameters(getLogger(__name__))

employees_router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
    responses={400: {"description": "Bad request"}, 404: {"description": "Not found"}},
    dependencies=[Depends(check_secret_token)],
)


@employees_router.get("/", status_code=200, response_model=GetEmployeesResponse)
async def get_employees(feature: Optional[str], value: Optional[str], option: Optional[str] = None):
    """
    Get employees filtering by feature.
    ### Input
    * **feature**: Query parameter to indicate by which feature we have to filter.
    * **value**: Query parameter to indicate what value for feature we have to use in filtering.
    * **option**: Query parameter to indicate option for filtering. Possible are: "lt", "lte", "gt", "gte".

    ### Output
    * List of employees objects.
        employees object:
        * **name**: employee's name.
        * **email**: employee's email.
        * **age**: employee's age.
        * **company**: employee's company.
        * **join_date**: String-representation of the employee's join date.
        * **job_title**: employee's job title.
        * **gender**: employee's gender.
        * **salary**: employee's salary.

    """
    # TODO: Дополнительно можно добавить пагинацию, чтобы возвращать найденных сотрудников небольшими батчами.
    # Для этого можно добавить еще два query-параметра: page и pagesize,
    # определяющие номер страницы и ее объем соответственно.
    LOGGER.info("Get employees called, feature: %s, value: %s, option: %s", feature, value, option)
    if feature not in Employee.__fields__:
        raise HTTPException(
            status_code=400,
            detail="Wrong feature. Must be one of {name, email, age, company, join_date, job_title, gender, salary}",
        )

    if option and option not in {"lt", "lte", "gt", "gte"}:
        raise HTTPException(status_code=400, detail="Wrong value for option. Must be one of {lt, lte, gt, gte}")

    if option and feature not in {"age", "join_date", "salary"}:
        raise HTTPException(
            status_code=400,
            detail="This feature can not be used with option."
            "Applicable features with option are: age, join_date, salary",
        )

    employees_list = await employees_crud.read_employees(feature=feature, value=value, option=option)
    LOGGER.info("Get employees completed, returned %s employees.", len(employees_list))
    return employees_list
