num = 1
num1 = 0
num2 = 1
import time
for i in range(0, 1000):
    print(num)
    num = num1 + num2
    num1 = num2
    num2 = num
    time.sleep(0.00000001)
