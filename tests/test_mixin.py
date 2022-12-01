def test_dataclass_with_mixin_are_instance_of_dict(a_dataclass):
    assert isinstance(a_dataclass, dict)


def test_dataclass_with_mixin_can_access_attribute_like_a_dictionary(a_dataclass):
    assert a_dataclass["attribute1"] == "attr1"


def test_dataclass_with_mixin_can_access_attribute_like_a_dataclass(a_dataclass):
    assert a_dataclass.attribute1 == "attr1"


def test_dataclass_with_mixin_can_be_compare_for_equality_with_a_dict(a_dataclass, a_dict):
    assert a_dataclass == a_dict
    assert a_dict == a_dataclass


def test_dataclass_with_mixin_can_add_key_value(a_dataclass):
    a_dataclass["new_attribute"] = "NEW"
    assert a_dataclass.new_attribute == "NEW"
    assert a_dataclass["new_attribute"] == "NEW"


def test_dataclass_with_mixin_can_add_attribute(a_dataclass):
    a_dataclass.new_attribute = "NEW"
    assert a_dataclass["new_attribute"] == "NEW"
    assert a_dataclass.new_attribute == "NEW"


def test_dataclass_with_mixin_can_return_all_items(a_dataclass):
    k = a_dataclass.items()
    assert set(k) == set([("attribute1", "attr1")])


def test_dataclass_with_mixin_delete_a_key_value(a_dataclass):
    del a_dataclass["attribute1"]
    assert "attribute1" not in a_dataclass
    assert not hasattr(a_dataclass, "attribute1")


def test_dataclass_with_mixin_delete_an_attributes(a_dataclass):
    del a_dataclass.attribute1
    assert "attribute1" not in a_dataclass
    assert not hasattr(a_dataclass, "attribute1")
