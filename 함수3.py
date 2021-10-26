def return_example(a, b):
    if a > b:
        print("a")
        return
    else:
        print("b")
    print("adios")


print(return_example(20, 10))
print(return_example(10, 20))
