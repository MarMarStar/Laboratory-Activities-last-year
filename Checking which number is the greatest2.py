a = int(input("enter number a "))
b = int(input("enter number b "))
c = int(input("enter number c "))

if a > b and a > c:
    print(("a is greatest"))

elif b > a and b > c:
    print(("b is greatest"))
    
elif c > a and c > b:
    print(("c is the greatest"))
    
elif a == b == c:
    print(("All are equal!"))

elif b == c or b == a or c == a or c == b:
    print(("No number is greatest. 2 or more have equal amount"))