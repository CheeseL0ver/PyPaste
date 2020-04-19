echo ''
echo 'Starting tests...'
echo 'Testing' | python3 test.py
test_status=$(echo $?)

exit $test_status