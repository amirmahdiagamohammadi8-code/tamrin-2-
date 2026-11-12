def check_access (**kwargs) :
    if "email" in kwargs and "name" in kwargs :
        if "admin" not in kwargs   or kwargs["admin"] == False :
            print("Access Denied")
            return
        
        if kwargs["admin"] == True :
            print("Access Granted ")

        for i in kwargs :
           key = i,kwargs[i]
           print(key)
           
check_access(name ="amir",email="gvuiv",admin=True)