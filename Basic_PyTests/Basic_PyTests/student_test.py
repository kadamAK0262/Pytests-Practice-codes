from student import StudentDB
import pytest

db=None

# run before each test function to which it is applied. After fixture we do not need setup module
@pytest.fixture
# @pytest.fixture(scope='module')
def db():
    print("____Setup Module____")
    global db 
    db = StudentDB()
    db.connect('data.json')
    return db

# For Fixture
def test_akshay_data(db):
    akshay_data = db.get_data('Akshay')
    assert akshay_data['id'] == 1
    assert akshay_data['name'] == 'Akshay'
    assert akshay_data['result'] == 'Pass'

def test_wolf_data(db):
    wolf_data = db.get_data('Whitewolf')
    assert wolf_data['id'] == 2
    assert wolf_data['name'] == 'Whitewolf'
    assert wolf_data['result'] == 'Fail'

# # This setup module runs before execution of tests 
# def setup_module(module):
#     print("____Setup Module____")
#     global db 
#     db = StudentDB()
#     db.connect('data.json')

# #This Teardoen module runs after complition of tests
# def teardown_module(module):
#     print("----Teardown Module-----")

# #Without fixture 
# def test_akshay_data():
#     akshay_data = db.get_data('Akshay')
#     assert akshay_data['id'] == 1
#     assert akshay_data['name'] == 'Akshay'
#     assert akshay_data['result'] == 'Pass'

# def test_wolf_data():
#     wolf_data = db.get_data('Whitewolf')
#     assert wolf_data['id'] == 2
#     assert wolf_data['name'] == 'Whitewolf'
#     assert wolf_data['result'] == 'Fail'

    
