import openpyxl
import pytest


def get_data():


    for r in range(2, total_rows + 1):
        row_list = []
        for c in range(1, total_cols + 1):
            row_list.append(sheet.cell(r, c).value)
        final_list.append(row_list)
    return final_list


@pytest.mark.parametrize("username,password", get_data())
def test_login(username, password):
    print('logged in using username: ' + username + ' and password:' + password)
