/piscine_python/python00/ex09/README.md
# ft_package

A sample test package for counting items in lists.

## Installation

```bash
pip install ft_package
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```