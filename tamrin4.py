import time 
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        ekhtelaf = end - start
        print(f"زمان اجرا: {ekhtelaf:.2f} ثانیه")
        return result
    return wrapper

@calculate_time
def create_order (*args,**kwargs) :

    count = 0
    for i in args :
        count = count + 1
    print(f"count : {count}")

    print (args)
    print(kwargs)

    report_text = f"Customer: {kwargs.get('name')}\nAddress: {kwargs.get('address')}\nProducts: {args}\nTotal Products: {count}\n"
    with open("orders.txt", "w", encoding="utf-8") as file:
        file.write(report_text)

create_order( 
"Laptop", 
 "Mouse",
 "Keyboard", 
name="Ali", 
 address="Tehran"
)