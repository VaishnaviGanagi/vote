try:
  age=int(input("Enter age:"))
  if age >= 18:
    print("eligible to vote")
  else:
    print("not eligible")
except ValueError:
  print("enter valid integer")
