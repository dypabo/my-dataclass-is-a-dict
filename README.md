# my_dataclass_is_a_dict

my_dataclass_is_a_dict is a library to force a dataclass to act like a dictionary

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install my_dataclass_is_a_dict.

```bash
pip install my_dataclass_is_a_dict
```

## Usage

```python
from dataclasses import dataclass
from my_dataclass_is_a_dict import DictionaryMixin

@dataclass
class MyDataclass(DictionaryMixin):
    attribute1: str
    attribute2: str

instance = MyDataclass("attr1", 123)
assert instance["attribute1"] == "attr1"
assert instance["attribute2"] == 123
repr(instance)  # "MyDataclass(attribute1='attr1', attribute2=123)"
```

### dunder repr

Calling repr on the dataclass will be in the format of a dataclass.
If you need to have the dictionary repr output, add repr=False when creating your dataclass


```python
from dataclasses import dataclass
from my_dataclass_is_a_dict import DictionaryMixin

@dataclass(repr=False)
class MyDataclass(DictionaryMixin):
    attribute1: str
    attribute2: str

instance = MyDataclass("attr1", 123)
repr(instance)  # "{attribute1='attr1', attribute2=123}"
```


