#pytest testSentimentAnalyzer.py

from main2 import app
from fastapi.testclient import TestClient

client = TestClient(app)
access_token = "1234567asdfgh"
def test_read_item_bad_token1():
    response = client.get("/deanonymize?user_input=NKE")
    assert response.status_code == 200

def test_read_item_bad_token2():
    response = client.get("/displayPIIEntitywithStar?UserInput=AGEN")
    assert response.status_code == 200

def test_read_item_bad_token3():
    response = client.get("Authentication?usrName=jayshil&usrPassword=jain")
    assert response.status_code == 200

def test_read_item_bad_token4():
    response = client.get("/sentiment?UserInput=AGEN")
    assert response.status_code == 200
 
def test_read_item_bad_token5():
    response = client.get("/deanonymize?user_input=AGEN")
    assert response.status_code == 200

# def test_read_item_bad_token2():
#     response = client.get("/getcolumnvalues/FILE_NAME", headers={"access_token": access_token})
#     assert response.status_code == 200
# def test_read_item_bad_token3():
#     response = client.get("/getexperimentdatamachine/2/Prep", headers={"access_token": access_token})
#     assert response.status_code == 200
# def test_read_item_bad_token4():
#     response = client.get("/knowexpwornstatus/worn", headers={"access_token": access_token})
#     assert response.status_code == 200
# def test_read_item_bad_token5():
#     response = client.get("/getdatatool/worn", headers={"access_token": access_token})
#     assert response.status_code == 200
# def test_read_item_bad_token6():
#     response = client.get("/knowexppassvisual/no", headers={"access_token": access_token})
#     assert response.status_code == 200
# def test_read_item_bad_token7():
#     response = client.get("/getdatavisualinspection/no", headers={"access_token": access_token})
#     assert response.status_code == 200
# def test_read_item_bad_token8():
#     response = client.get("/knowexpmachiningfinalized/yes", headers={"access_token": access_token})
#     assert response.status_code == 200
# def test_read_item_bad_token9():
#     response = client.get("/getdatamachiningfinalized/no", headers={"access_token": access_token})
#     assert response.status_code == 200
# def test_len_item_bad_token1():
#     response = client.get("/getexpcnc/1", headers={"access_token": access_token})
#     assert len(response.json()) == 1517469
# def test_len_item_bad_token2():
#     response = client.get("/getcolumnvalues/FILE_NAME", headers={"access_token": access_token})
#     assert len(response.json()) == 18
# def test_len_item_bad_token3():
#     response = client.get("/getexperimentdatamachine/2/Prep", headers={"access_token": access_token})
#     assert len(response.json()) == 220734
# def test_len_item_bad_token4():
#     response = client.get("/knowexpwornstatus/worn", headers={"access_token": access_token})
#     assert len(response.json()) == 56
# def test_len_item_bad_token5():
#     response = client.get("/getdatatool/worn", headers={"access_token": access_token})
#     assert len(response.json()) == 19107642
# def test_len_item_bad_token6():
#     response = client.get("/knowexppassvisual/no", headers={"access_token": access_token})
#     assert len(response.json()) == 21
# def test_len_item_bad_token7():
#     response = client.get("/getdatavisualinspection/no", headers={"access_token": access_token})
#     assert len(response.json()) == 5658061
# def test_len_item_bad_token8():
#     response = client.get("/knowexpmachiningfinalized/yes", headers={"access_token": access_token})
#     assert len(response.json()) == 78
# def test_len_item_bad_token9():
#     response = client.get("/getdatamachiningfinalized/no", headers={"access_token": access_token})
#     assert len(response.json()) == 3090279
