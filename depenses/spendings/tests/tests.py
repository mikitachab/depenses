

def test_env(client):
    resp = client.get("/")
    assert resp.status_code == 200
