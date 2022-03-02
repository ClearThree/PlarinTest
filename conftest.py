import pytest

from fastapi.testclient import TestClient

from app.main import app
from app.utils.dependencies import check_secret_token


async def return_true():
    return True


@pytest.fixture(scope="module")
def test_app():
    app.dependency_overrides[check_secret_token] = return_true
    with TestClient(app) as test_client:
        yield test_client
