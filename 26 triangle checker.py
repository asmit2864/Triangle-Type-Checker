a=int(input("x:"))
b=int(input("y:"))
c=int(input("z:"))

if a==b==c:
    print("Triangle is equilateral")
elif a==b or b==c or a==c:
    print("Triangle is Isosceles")
else:
    print("Scalene Triangle")