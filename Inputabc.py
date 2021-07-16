# input for a, b, and c with its exception handling and keeping the raw error from end user view
while True: 
    try:
        a = int(input("Enter value a: "))
        break
    except Exception:
        print('Invalid input a, not an integer please try again')
        pass
while True:  
    try:
        b = int(input("Enter value b: "))
        break
    except Exception:
        print('Invalid input a, not an integer please try again')
        pass
while True:  
    try:
        c = int(input("Enter value c: "))
        break
    except Exception:
        print('Invalid input a, not an integer please try again')
        pass
# Comparison of the the inputs a, b, and c collected
if a == b == c:
    print('equal')
else: 
    print('not equal')