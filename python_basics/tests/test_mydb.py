import pytest

from mydb import MyDB


@pytest.fixture(scope="module")
def cur():
    print("settings up")
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()
    yield cur
    cur.close()
    conn.close()
    print("connection closed")


def test_john_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123


def test_tom_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 456
