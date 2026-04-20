def test_create_task(client, token):
    res = client.post("/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Test Task",
            "description": "Testing"
        }
    )
    assert res.status_code == 201


def test_get_tasks(client, token):
    client.post("/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Task1", "description": "Demo"}
    )

    res = client.get("/tasks",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200
    assert isinstance(res.json, list)


def test_update_task(client, token):
    # create first
    client.post("/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Task1", "description": "Demo"}
    )

    res = client.put("/tasks/1",
        headers={"Authorization": f"Bearer {token}"},
        json={"status": "completed"}
    )

    assert res.status_code == 200


def test_delete_task(client, token):
    client.post("/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Task1", "description": "Demo"}
    )

    res = client.delete("/tasks/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200


def test_unauthorized_access(client):
    res = client.get("/tasks")
    assert res.status_code == 401