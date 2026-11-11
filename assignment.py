# Assignment on nested if else 

security_code=int(input("Enter the security code:"));
if security_code==5566:
    department=input("Enter your department:");
    if department=='Finance':
        access_level=int(input("Enter your access_level:"));
        if access_level>=5:
            print("Access Granted! Welcome to meeting room");
        else:
            print("Insufficient access level!");
    else:
        print("Access denied:department not allowed");
else:
    print("Invalid Security code");
