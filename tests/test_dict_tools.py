from flat_nest_pydict import example_nested_dict, example_flat_dict
from flat_nest_pydict import flatten, nest


def test_should_flatten_nested_dict():
    # given
    nested_dict = example_nested_dict()
    flat_dict = example_flat_dict()
    # when
    result_dict = flatten(nested_dict)
    # then
    assert result_dict == flat_dict


def test_should_nest_flat_dict():
    # given
    nested_dict = example_nested_dict()
    flat_dict = example_flat_dict()
    # when
    result_dict = nest(flat_dict)
    # then
    assert result_dict == nested_dict


def test_nesting_and_flattening_should_be_reversible():
    # given
    nested_dict = example_nested_dict()
    # when
    result_dict = nest(flatten(nested_dict))
    # then
    assert result_dict == nested_dict


def test_flattening_and_nesting_should_be_reversible():
    # given
    flat_dict = example_flat_dict()
    # when
    result_dict = flatten(nest(flat_dict))
    # then
    assert flat_dict == result_dict
