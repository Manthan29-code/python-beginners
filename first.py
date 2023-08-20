import datetime
print("Enter your name")
name=input()
print("Enter your born year")
year=int(input())
age=(datetime.date.today().year) - year
print("Yoyr age is",age)