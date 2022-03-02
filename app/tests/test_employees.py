def test_app_is_alive(test_app):
    res = test_app.get("/ping")
    assert res.status_code == 200
    assert res.json() == "pong"


def test_get_employee_by_name(test_app):
    res = test_app.get("api/v1/employees/?feature=name&value=Vadim")
    assert res.status_code == 200
    assert not res.json()


def test_get_employee_by_salary(test_app):
    res = test_app.get("api/v1/employees/?feature=salary&value=9632&option=gt")
    assert res.status_code == 200
    assert len(res.json()) == 23


def test_get_employee_by_salary_gte(test_app):
    res = test_app.get("api/v1/employees/?feature=salary&value=9632&option=gte")
    assert res.status_code == 200
    assert len(res.json()) == 24


def test_get_employee_by_date_joined(test_app):
    res = test_app.get("api/v1/employees/?feature=join_date&value=2009-06-10T19:08:52-07:00&option=gte")
    assert res.status_code == 200
    assert len(res.json()) == 177


def test_wrong_feature_passed(test_app):
    res = test_app.get("api/v1/employees/?feature=unexisting&value=1337")
    assert res.status_code == 400
    assert res.json()["detail"].startswith("Wrong feature.")


def test_option_passed_with_wrong_feature(test_app):
    res = test_app.get("api/v1/employees/?feature=name&value=Cedric%20Page&option=lt")
    assert res.status_code == 400
    assert res.json()["detail"].startswith("This feature can not be")


def test_wrong_option(test_app):
    res = test_app.get("api/v1/employees/?feature=salary&value=25&option=zz")
    assert res.status_code == 400
    assert res.json()["detail"].startswith("Wrong value")


def test_empty_response(test_app):
    res = test_app.get("api/v1/employees/?feature=name&value=Vadim")
    assert res.status_code == 200
    assert res.json() == []
