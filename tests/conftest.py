from dataclasses import dataclass

from pytest import fixture

from my_dataclass_is_a_dict import DictionaryMixin


@dataclass
class ADataclass(DictionaryMixin):
    """test class"""

    attribute1: str


@dataclass(repr=False)  # repr call will be from the dictionary
class ADataclassNoRepr(DictionaryMixin):
    """test class without repr method"""

    attribute1: str


@fixture
def a_dataclass():
    return ADataclass("attr1")


@fixture
def a_dataclass_no_repr():
    return ADataclassNoRepr("attr1")


@fixture
def a_dict():
    return {"attribute1": "attr1"}
