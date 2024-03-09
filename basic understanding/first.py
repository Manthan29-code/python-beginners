from datetime import date

print("Enter your name")
name=input()
print("Enter your birth year")
year=int(input())
age=(date.today().year) - year
print("Yoyr age is",age)