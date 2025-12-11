import app

def test_hola_mundo():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Hola Mundo" in response.data.decode()
