import pytest
import requests
from test_data import valid_credentials,invalid_credentials

BASE_URL = "https://route.comm100standby.io/api/v1/router/agents/getByEmail/?partnerId=10000&email="

@pytest.mark.parametrize("credentials", valid_credentials)
def test_login_successful(credentials):
    response = requests.get(BASE_URL+credentials.get("email"))
    assert response.status_code == 200

@pytest.mark.parametrize("credentials", invalid_credentials)
def test_login_failed(credentials):
    print(credentials.get("email"))
    response = requests.get(BASE_URL+credentials.get("email"))
    assert response.status_code == 200
    rjson= response.json()
    assert rjson.get("errorCode")==100
    assert rjson.get("errorMessage")=="Email or password is incorrect."

