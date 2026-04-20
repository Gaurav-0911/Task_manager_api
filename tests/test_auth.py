def test_register(client):
    res = client.post("/register", json={
        "username": "gaurav",
        "password": "1234"
    })
    assert res.status_code == 201


def test_login(client):
    # first register
    client.post("/register", json={
        "username": "gaurav",
        "password": "1234"
    })

    # then login
    res = client.post("/login", json={
        "username": "gaurav",
        "password": "1234"
    })

    assert res.status_code == 200
    assert "access_token" in res.json