import time

def calculate_time(func):
    def wrapper():
        start=time.time()
        result = func()
        end = time.time()


        ekhtelaf = end - start

        round_ekhtelaf = round(ekhtelaf,2) 

        print(ekhtelaf)
        return result 
    return wrapper

@calculate_time
def say_hello():
    time.sleep(1.2345)
    print("سلام!")

say_hello()