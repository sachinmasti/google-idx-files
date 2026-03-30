sm = open('/home/user/interstellar/pycal/cal.py','r')
sm1= sm.read()
print(sm1)
sm.close()

with open("/home/user/interstellar/pycal/cal.py",'r') as f:
    print(f.read())
f.close()

# with open('/home/user/interstellar/pycal/cal.py','a') as s:
#     print(s.write('hello'))
# s.close()

import os

s = os.listdir('/home/user/interstellar/problem_practice.py')
print(s)
print(os.getcwd())
# with os.listdir('/home/user/interstellar/problem_practice.py') as sm:
#     print(sm)