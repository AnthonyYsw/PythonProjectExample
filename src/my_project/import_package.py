# Import package (directory) example
import package
from package import *

print(package.__version__)
print(package.__author__)

x = package.recursion.factorial(5)
print(x)
y = recursion.fibonacci(10)
print(y)