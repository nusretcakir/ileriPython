import time



def decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(round(end-start,2) , " second")
    return wrapper

@decorator
def fonksiyon():
    time.sleep(1.45)
    print("heyheyyy")
    

fonksiyon()