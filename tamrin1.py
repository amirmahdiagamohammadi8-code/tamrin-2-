def numbers (*args):
    if len(args) == (0):
        return" You do not enter number ."
    count=0
    total =0
    miangin = 0
    for i in args :
        total = total + i
         
        count = count +1



    miangin = total / count

    numbers_max = (max(args))

    numbers_min = (min(args))


    return f"""    total :{total} 
    count :{count} 
    min :{numbers_min}
    max : {numbers_max}
    miangin : {miangin}"""


    
javab = numbers(10,11,12)
print(javab)
