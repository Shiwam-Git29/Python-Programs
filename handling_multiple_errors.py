try:
    x=int(input("Enter x:"))
    y=10/x
except ValueError:
    print("Please Enter a valid Number:")
except ZeroDivisionError:
    print("Division by Zero is not allowed")
finally:
    print("i will always run")
