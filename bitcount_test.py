from bitcount import bitcount
import json
import sys


def test_bitcoun():

    assert bitcount(14) == 3

    # json_data = open("/Users/wuyuxuan/research-local/QuixBugs/json_testcases/"+"bitcount"+".json", 'r')
    # for line in json_data:
    #         py_testcase = json.loads(line)
    #         print(py_testcase)
    #         test_in, test_out = py_testcase
    #         one_test(test_in, test_out)


            # try:
            #     assert bitcount(test_in) == test_out
            #     # print("pass")
            # except AssertionError as e:
            #     # e.args += ('not pass')
            #     # raise
            #     print("not pass")

            # assert bitcount(test_in) == test_out

# def one_test(test_in, test_out):
#     assert bitcount(test_in) == test_out
    # try:
    #     assert bitcount(test_in) == test_out
    #     # print("pass")
    # except AssertionError as e:

# def test2():
#     assert bitcount(128) == 1

def test3():
    assert bitcount(27) == 4

def test4():
    assert bitcount(13) == 3
        
            



# if __name__ == "__main__":
#     test_bitcoun()
#     test2()
    


