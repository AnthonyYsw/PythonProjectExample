import tomllib
from pprint import pprint
import os

# Import package example
import package
from package import *

print(package.__version__)
print(package.__author__)

x = package.recursion.factorial(5)
print(x)
y = recursion.fibonacci(10)
print(y)

# Load configuration from a TOML file
def load_toml() -> dict:
    """
    Load the configuration from a TOML file.
    """

    # Find config.toml
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    grandparent_dir = os.path.dirname(parent_dir)
    toml_path = os.path.join(grandparent_dir, 'config.toml')

    with open(toml_path, 'rb') as f:
        toml_data: dict = tomllib.load(f)
        return toml_data

    
if __name__ == "__main__":
    data: dict = load_toml()
    pprint(data, sort_dicts=False)
