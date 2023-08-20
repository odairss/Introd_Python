import time
x = 10
while x >= 0:
    print(x)
    x = x - 1
    time.sleep(1)

if x < 0:
    print("Fogo!")
