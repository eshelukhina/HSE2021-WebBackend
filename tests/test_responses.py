from fastapi.testclient import TestClient

from db.fake_db import data
from main import app

client = TestClient(app)


def test_get_by_id_OK():
    response = client.get("/Patients/id?patient_id=1")
    assert response.status_code == 200
    assert response.json() == data[1]


def test_get_by_id_ID_not_exist():
    not_exists_id = len(data) + 1
    response = client.get("/Patients/id?patient_id=" + str(not_exists_id))
    assert response.status_code == 400
    assert response.json() == {"detail": "Id does not exist"}


def test_add_patient_already_exists():
    for ids in data:
        response = client.post("/Patients/add_patient?patient_id=" + str(ids),
                               json={"name": data[ids]["name"],
                                     "age": data[ids]["age"],
                                     "gender": data[ids]["gender"],
                                     "diagnosis": data[ids]["diagnosis"]})
        assert response.status_code == 400
        assert response.json() == {"detail": "Patient already exist"}


def test_add_patient_OK():
    sz = len(data) + 1
    response = client.post("/Patients/add_patient?patient_id=" + str(sz),
                           json={"name": "Steve Jobs",
                                 "age": 56,
                                 "gender": "Male",
                                 "diagnosis": "Cancer"}
                           )
    assert response.status_code == 200
    assert response.json() == {
        "name": "Steve Jobs",
        "age": 56,
        "gender": "Male",
        "diagnosis": "Cancer"
    }


def test_add_patient_invalid_args_name():
    sz = len(data) + 1
    response = client.post("/Patients/add_patient?patient_id=" + str(sz),
                           json={"name": "Username",
                                 "age": 1000,
                                 "gender": "Male",
                                 "diagnosis": "OK"}
                           )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid patient params. Name must contains firstname and "
                  "lastname. Age must be >= 0"
    }


def test_add_patient_invalid_args_age():
    sz = len(data) + 1
    response = client.post("/Patients/add_patient?patient_id=" + str(sz),
                           json={"name": "Firstname Lastname",
                                 "age": -1,
                                 "gender": "Female",
                                 "diagnosis": "OK"}
                           )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid patient params. Name must contains firstname and "
                  "lastname. Age must be >= 0"
    }
