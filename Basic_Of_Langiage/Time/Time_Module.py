import time

def WhileLoop():
    i = 0 
    while(i < 500):
        i = i + 1
        print(i)

def ForLoop():
    for i in range(500):
        print(i)

init = time.time()
WhileLoop()
print("While Loop\t",time.time() - init)
ForLoop()
init = time.time()
print("For Loop\t",time.time() - init)

# print(5)
# time.sleep(3)
# print("Sleeping")
# print("Full")

# t = time.localtime()
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

# print(formatted_time) 