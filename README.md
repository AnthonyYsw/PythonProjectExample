# Python Project Example

<span style="color:red">
This project is intended solely for learning purposes. It is provided as a reference for anyone wishing to organise their Python projects in a systematic manner; it is neither a standard nor a perfect structure. All content is based on personal understanding, so if you spot any errors, your feedback is most welcome.
</span>


This project gives an example of structuring a Python project. The aim is to make your Python programme easier to be maintained, structured, and extensible.

You will se multiple directories stack with each other, DON'T PANIC! I will breakdown them and explain each file. (Also with some methodologies used in Python.)

## `README.md`

`README.md` is similar to abstract when you are writing a article, it gives people a idea of what this project done without struggling the complex code and structures. So introduce the project briefly, and make more developers interested in it. 

With the assistance of `.md` format, you can also insert images formats in your documents to make it more visualised. 

## LICENSE

Choose a suitable `LICENSE` file is essential for project distribution, and the copyrights.

Recommendations for Choosing a Licence:

* For maximum distribution: choose MIT or BSD
* If you require patent protection: choose Apache 2.0
* To ensure your code remains open-source forever: choose GPL
* To balance open-source and commercial interests: choose MPL 2.0
* To completely relinquish copyright: choose Unlicense or CC0

## `environment.yml`

This is the environment configuration file for running the programmes. Can be generated in your shell. 

eg. if you want generate from conda, type:
`conda env export --no-builds > environment.yml`, This will create a file named `environment.yml` in your current directory. And people can install the environment by typing: `conda env create -f environment.yml 
`.

this `.yaml` file can be named differently, like `environments.yml`, `requirements.yml`, etc.

For other package manager like `pip`, you can view more method at [pipreqs](https://github.com/bndr/pipreqs).

## `config.toml`

`config.toml` is a text file for storing configuration items in [TOML (Tom's Obvious, Minimal Language)](https://toml.io/) format. Compared with JSON and YAML, TOML has a concise and readable syntax, which makes it ideal for project configuration management.

Commonly used for global configuration of an application or service, project build tools or script parameters, and initialization options for third-party libraries.

For different projects and different usages, `config.toml` file can be different, so I will suggest you to find a suitable content by yourself or with your teammates. I give you a example format of it.

## `.gitignore`

When you are managing your codes and files, it's inevitable to use [git](https://git-scm.com/). `.gitignore` file gives a rule of choosing files to commit. However, if you're not using git, ignore this file.

You can find typical `.gitignore` file in [gitignore](https://github.com/github/gitignore.git), adjust the file when necessary.

## Main Body of Python Project

### `src/`

The `src/` directory stores all the important codes. One recommend structure is:

```
src/
├── my_project/
│   ├── package/
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── pkg_function_1.py
│   │   ├── pkg_function_2.py
│   │   └── ...
│   ├── config.py
│   ├── main.py
│   ├── main_function_1.py
│   ├── main_function_2.py
│   └── ...
├── test/
│   ├── test_package/
│   │   └── (similar)
│   ├── config.py
│   ├── test_main.py
│   ├── test_function_1.py
│   └── ...
```

`my_project/` and `test/` are two main directories, `my_project/` is a stable version that will be released, and `test/` is test. They have similar structures. You can also create feature directories (like `feature_1/`) in parallel with these two.

I will explain the `my_project/` as an example. 

the `main.py` is where you run you whole programme, it should be kept as clear and simple as possible, and only saves the main function and imports other modules.

The main operation could be written separately. For example, if you write a data processing and plot function in a single file, it works. However, the documentation is too lengthy and is not easy to maintain when a bug occurs, as it is necessary to find the exact location of the error, especially for large projects. Instead, I seperate the functions in few `.py` files. Then you can link the functions simply by:

```
import <filename1>
from <filename2> import <variable_in_file2>
```

and use them like using 3rd-party packages like Numpy, Matplolib, etc.

Besides, a `config.py` is recommended, you can initialise your programme and make some presets here, like I import the information of `config.toml` here.

Another technique in Python I can briefly go through here is grouping up functions and store them in a folder, I call it `pakage/` here. It can has a `README.md` file if you like. It must contains a `__init__.py` file, the interpreter will recognise it as an package instead of a common directory. It can also initialise the package, define the public interface of a package (e.g., specify the names of exportable submodules in the `__all__` list), import submodules or packages, and simplify external calls. 

I give you an example of creating a package here:

`__init__.py`:

One common structure can be:

1. define the information of packages

```
__version__ = "1.0.0"
__author__ = "Anthony"
__email__ = "anthony.yang.22@ucl.ac.uk"
```

2. linking part, import the sub-modules into the namespace

```
from . import <submodule1>
from . import <submodule2>
...
```

3. Perform a “wildcard” import of everything that each sub-module.
   
```
from .<submodule1> import *
from .<submodule2> import *
...
```

4. define `__all__` so that you can perform `from <package> import *` when using the pakcage. `__all__` defines the package-level metadata, and `__all__.extend()` add the sub-module name to the public API.

```
__all__ = ["__version__", "__author__", "__email__"]
__all__.extend(["recursion", "basic_math"])
```

In this given example, after `from <package> import *`, you can use the function like `package.recursion.factorial()` or `recursion.factorial()`. BUT be careful with common name when you have many packages.

### `data/`

It's annoying to put the code files and data files together, especially when you have enormous data files. Put them in a folder helps organisation!

### other folders

Other folders like `imgs/` is helpful. If you are managing a LaTeX project, you will definetly benefit from it.

Add more if it's necessary.