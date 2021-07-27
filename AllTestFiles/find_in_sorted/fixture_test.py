from find_in_sorted import find_in_sorted
import json
import sys
import pytest

name = "find_in_sorted"
# def test_bitcoun():

def get_data():
    working_file = open("/Users/wuyuxuan/research-local/QuixBugs/json_testcases/"+name+".json", 'r')

    for line in working_file:
        py_testcase = json.loads(line)
        # print(py_testcase)
        test_in, test_out = py_testcase
        if not isinstance(test_in, list):
            # input is required to be a list, as multiparameter algos need to deconstruct a list of parameters
            # should fix in testcases, force all inputs to be list of inputs
            test_in = [test_in]

        yield test_in, test_out

# def printdata():
#     mygenerate = get_data()
#     print(mygenerate)

@pytest.fixture(params=get_data())
def line_fixture(request):
    return request.param

def test_(line_fixture):
    # print(line_fixture[1])
    assert find_in_sorted(line_fixture[0][0], line_fixture[0][1]) == line_fixture[1]

# def test_bitcount(input_x, expected):
#     assert bitcount(input_x) == expected

#     assert bitcount(14) == 3
#
#     # json_data = open("/Users/wuyuxuan/research-local/QuixBugs/json_testcases/"+"bitcount"+".json", 'r')
#     # for line in json_data:
#     #         py_testcase = json.loads(line)
#     #         print(py_testcase)
#     #         test_in, test_out = py_testcase
#     #         one_test(test_in, test_out)
#
#
#             # try:
#             #     assert bitcount(test_in) == test_out
#             #     # print("pass")
#             # except AssertionError as e:
#             #     # e.args += ('not pass')
#             #     # raise
#             #     print("not pass")
#
#             # assert bitcount(test_in) == test_out
#
# # def one_test(test_in, test_out):
# #     assert bitcount(test_in) == test_out
#     # try:
#     #     assert bitcount(test_in) == test_out
#     #     # print("pass")
#     # except AssertionError as e:
#
# # def test2():
# #     assert bitcount(128) == 1
#
# def test3():
#     assert bitcount(27) == 4
#
# def test4():
#     assert bitcount(13) == 3





# if __name__ == "__main__":
#     printdata()
