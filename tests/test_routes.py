from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api_healthCheck")
    assert response.status_code == 200
    assert response.json() == {"message": "health Check"}


def test_register():
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "password": "password123",
        "email": "john@example.com"
    }
    response = client.post("/register", json=data)
    assert response.status_code == 200
    assert "user_id" in response.json()


def test_login():
    data = {
        "user_id": "test420240226112239",
        "password": "test1234"
    }
    response = client.post("/login", json=data)
    assert response.status_code == 200
    assert "access_token" in response.json()
    print(response.json()['access_token'])


def test_create_room():
    data = {
        "room_name": "Test Room",
        "currency": "USD",
        "members": ["test420240226112239", "test520240226113222", "test620240226113304"]
    }
    headers = {"Authorization": "Bearer {}".format(login())}
    response = client.post("/createRoom", json=data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {'new_room': 'Test Room'}


def test_search_rooms():
    headers = {"Authorization": "Bearer {}".format(login())}
    response = client.get("/getRoomsForUser", headers=headers)
    assert response.status_code == 200
    assert 'User test420240226112239 found inside the following rooms' in response.json()
    assert isinstance(response.json()['User test420240226112239 found inside the following rooms'], list)


def test_add_transactions():
    data = {
        "room_id": "room6",
        "amount": 100,
        "expense_name": "Grocery",
        "fairsplit_members": ["test520240226113222", "test620240226113304"]
    }
    headers = {"Authorization": "Bearer {}".format(login())}
    response = client.post("/addTransactions", json=data, headers=headers)
    assert response.status_code == 200
    assert response.json() == {'message': 'Expense added successfully'}


def test_show_transactions_under_room():
    data = {"room_id": "room5"}
    headers = {"Authorization": "Bearer {}".format(login())}
    response = client.post("/showTransactionsUnderRoom", json=data, headers=headers)
    assert response.status_code == 200
    assert "room_transaction_details" in response.json()


def test_settle_room_transaction_endpoint():
    data = {"room_id": "room_id_here"}
    headers = {"Authorization": "Bearer {}".format(login())}
    response = client.post("/settleUp", json=data, headers=headers)
    assert response.status_code == 200
    assert "settle_statements" in response.json()


def login():
    data = {
        "user_id": "test420240226112239",
        "password": "test1234"
    }
    response = client.post("/login", json=data)
    return response.json()['access_token']
