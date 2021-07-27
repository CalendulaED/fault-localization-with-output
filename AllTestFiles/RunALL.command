#!/bin/bash

#edit this to repo path
cd /Users/wuyuxuan/research-local/pytest_simple_example

#bitcount
cd bitcount
pytest --localize bitcount fixture_test.py
cd ..

#bucketsort
cd bucketsort
pytest --localize bucketsort fixture_test.py
cd ..

#find_in_sorted
cd find_in_sorted
pytest --localize find_in_sorted fixture_test.py
cd ..

#
