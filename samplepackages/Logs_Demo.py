import pytest
@pytest.mark.parametrize("username,password",[["123@gmail.com","123"],["456@gmail.com","456"],["789@gmail.com","789"]])
def test_login(username,password):
    print("logged in username:"+username+" and password:"+password)



