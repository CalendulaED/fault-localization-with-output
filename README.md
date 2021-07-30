# fault-localization-with-output
pytest fault-localization with the additional function that generate a csv file in the testing directory
This is the modified version from the post: https://github.com/hchasestevens/fault-localization
This fault localization will generate a csv with code line and their correspoding suspicious rate, which chould help with further research.

The test case is edit and modified from this orginal Benchmark: https://github.com/jkoppel/QuixBugs

Download fault-localization follow:https://github.com/hchasestevens/fault-localization
then, use pip3 show fault-localization to locate the file position, then replace the fault-localization file with current repo fault-localization folder.


Run:
`pytest --localize bitcount bitcount_test.py`

To see more sepcific usage, visit: https://github.com/hchasestevens/fault-localization

![image](https://user-images.githubusercontent.com/68514251/125785524-8be3ea0f-2d0d-4160-85d4-ff0301898416.png)


Double lick RunALL file to run all current available test file and generate their corresponding results.
