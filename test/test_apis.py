from main import app

def test_health():
    """health request test
    """
    response = app.test_client().get("/health")
    assert response.status_code == 200

def test_uname():
    response = app.test_client().get("/uname")
    assert response.status_code == 200

def test_service_redirect():
    response = app.test_client().get("/service")
    assert response.status_code == 400
