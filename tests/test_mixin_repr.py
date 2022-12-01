from pytest import raises


# ######################################################################
# Dataclass define with repr set to FALSE


def test_dataclass_no_repr_with_mixin_repr_method(a_dataclass_no_repr, a_dict):
    assert repr(a_dict) == repr(a_dataclass_no_repr)


def test_dataclass_no_repr_with_mixin_str_method_fallback_to_repr(a_dataclass_no_repr, a_dict):
    assert str(a_dict) == str(a_dataclass_no_repr)
    assert repr(a_dataclass_no_repr) == str(a_dataclass_no_repr)


def test_dataclass_no_repr_with_mixin_do_not_raise_when_calling_repr_after_deleting_a_key(
    a_dataclass_no_repr,
):
    """CAN use repr if a dataclass original attribute is deleted"""
    del a_dataclass_no_repr["attribute1"]
    assert repr(a_dataclass_no_repr) == "{}"


# #############################################################################
# Dataclass define with repr unspecified (automatically added by the dataclass)


def test_dataclass_with_mixin_repr_method_default(a_dataclass):
    assert repr(a_dataclass).startswith(a_dataclass.__class__.__name__)
    assert "attribute1" in repr(a_dataclass)
    assert "attr1" in repr(a_dataclass)


def test_dataclass_with_mixin_str_method_default(a_dataclass):
    assert str(a_dataclass).startswith(a_dataclass.__class__.__name__)
    assert "attribute1" in str(a_dataclass)
    assert "attr1" in str(a_dataclass)


def test_dataclass_with_mixin_will_not_raise_when_calling_repr_after_deleting_a_new_key(
    a_dataclass,
):
    """CAN use repr if a dataclass new attribute is deleted"""
    a_dataclass["new_attribute"] = "NEW"
    del a_dataclass["new_attribute"]
    repr(a_dataclass)


def test_dataclass_with_mixin_raise_when_calling_repr_after_deleting_a_key(a_dataclass):
    """CANNOT use repr if a dataclass original attribute is deleted"""
    del a_dataclass["attribute1"]
    with raises(AttributeError):
        repr(a_dataclass)
