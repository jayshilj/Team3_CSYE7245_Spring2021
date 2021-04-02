from fastapi.testclient import TestClient
from inferenceraw1 import API_KEY
from inferenceraw1 import app

client = TestClient(app)
#access_token = "1234567asdfgh"
access_token = API_KEY


def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    #print(type(response.json()))
    assert response.json() == "Welcome to CNC Mill APIs Homepage"


def test_read_item_bad_token1():
    response = client.get("/getexpcnc/3", headers={"access_token": access_token})
    assert response.status_code == 200
    #assert response.json() == {"detail": "Invalid X-Token header"}

def test_read_item_bad_token2():
    response = client.get("/getcolumnvalues/FILE_NAME", headers={"access_token": access_token})
    assert response.status_code == 200

def test_read_item_bad_token3():
    response = client.get("/getexperimentdatamachine/2/Prep", headers={"access_token": access_token})
    assert response.status_code == 200

def test_read_item_bad_token4():
    response = client.get("/knowexpwornstatus/worn", headers={"access_token": access_token})
    assert response.status_code == 200

def test_read_item_bad_token5():
    response = client.get("/getdatatool/worn", headers={"access_token": access_token})
    assert response.status_code == 200

def test_read_item_bad_token6():
    response = client.get("/knowexppassvisual/no", headers={"access_token": access_token})
    assert response.status_code == 200

def test_read_item_bad_token7():
    response = client.get("/getdatavisualinspection/no", headers={"access_token": access_token})
    assert response.status_code == 200

def test_read_item_bad_token8():
    response = client.get("/knowexpmachiningfinalized/yes", headers={"access_token": access_token})
    assert response.status_code == 200

def test_read_item_bad_token9():
    response = client.get("/getdatamachiningfinalized/no", headers={"access_token": access_token})
    assert response.status_code == 200
    #assert response.headers.get('content-length') == 3358245 

# def test_read_item1():
#     response = client.get("/cnc/1/Prep", headers={"access_token": access_token})
#     assert response.status_code == 200
#     # assert response.json() == {
#     #     "id": "foo",
#     #     "title": "Foo",
#     #     "description": "There goes my hero",
#     # 

# def test_read_inexistent_item():
#     response = client.get("/cnc/1/Prep", headers={"access_token": access_token})
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Item not found"}

