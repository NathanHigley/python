def quadratic_function(a,b,c):
    return lambda x : a*(x**2) + b*x + c

a1 = quadratic_function(1,2,1)
print(a1(1))
print("Input a,b and c from a quadratic equation in the form of")
print("f(x) = ax^2 + bx + c")

a = int(input("Input a : "))
b = int(input("Input b : "))
c = int(input("Input c : "))
x = int(input("Input x : "))
a2 = quadratic_function(a,b,c)
fx = a2(x)
print("f(x) = ",fx)
