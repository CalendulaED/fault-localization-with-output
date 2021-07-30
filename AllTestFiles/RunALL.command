#!/bin/bash

#edit this to repo path
cd /Users/wuyuxuan/research-local/pytest_simple_example/AllTestFiles

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

#get_factors
cd get_factors
pytest --localize get_factors fixture_test.py
cd ..

#Hanoi
cd hanoi
pytest --localize hanoi fixture_test.py
cd ..

#lcs_length
cd lcs_length
pytest --localize lcs_length fixture_test.py
cd ..

#levenshtein
cd levenshtein
pytest --localize levenshtein fixture_test.py
cd ..

#lis
cd lis
pytest --localize lis fixture_test.py
cd ..

#longest_common_subsequence
cd longest_common_subsequence
pytest --localize longest_common_subsequence fixture_test.py
cd ..

#max_sublist_sum
cd max_sublist_sum
pytest --localize max_sublist_sum fixture_test.py
cd ..

#next_palindrome
cd next_palindrome
pytest --localize next_palindrome fixture_test.py
cd ..

#next_permutation
cd next_permutation
pytest --localize next_permutation fixture_test.py
cd ..

#pascal
cd pascal
pytest --localize pascal fixture_test.py
cd ..

#powerset
cd powerset
pytest --localize powerset fixture_test.py
cd ..

#quicksort
cd quicksort
pytest --localize quicksort fixture_test.py
cd ..

#shunting_yard
cd shunting_yard
pytest --localize shunting_yard fixture_test.py
cd ..

#sieve
cd sieve
pytest --localize sieve fixture_test.py
cd ..

#subsequences
cd subsequences
pytest --localize subsequences fixture_test.py
cd ..

#to_base
cd to_base
pytest --localize to_base fixture_test.py
cd ..

#wrap
cd wrap
pytest --localize wrap fixture_test.py
cd ..
