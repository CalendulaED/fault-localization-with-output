# fault-localization-with-output
pytest fault-localization with the additional function that generate a csv file in the testing directory
This is the modified version from the post: https://github.com/hchasestevens/fault-localization
This fault localization will generate a csv with code line and their correspoding suspicious rate, which chould help with further research.

The test case is edit and modified from this orginal Benchmark: https://github.com/jkoppel/QuixBugs

Run:
`pytest --localize bitcount bitcount_test.py`

To see more sepcific usage, visit: https://github.com/hchasestevens/fault-localization
