x = int(input("x :"))
y = int(input("y :"))
z = int(input("z :"))
if x + y > z and x + z > y and z + y > x:
    print("تشکیل مثلث میدهد")
    if x == y == z:
        print("متساوی الاضلاع")
    elif x == y or x == z or z == y:
        print("متساوی الساقین")
    elif x != y != z:
        print("مختلف الاضلاع")
    if x**2 + y**2 == z**2 or y**2 +z**2 ==x**2 or x**2 + z**2 == y**2:
        print("قایم الزاویه")
else:
    print("تشکیل مثلث نمیدهد")