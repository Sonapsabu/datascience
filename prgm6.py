from datetime import datetime
first = datetime(2020, 1, 1)
second = datetime(2020,4,1)
 
if first < second:
        print('First date is less than the second date.')
elif first > second:
        print('First date is more than the second date.')
else:
        print('Both dates are the same.')
