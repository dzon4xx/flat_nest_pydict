# flat_nest_pydict
Flatten and nest python dictionary. After flattening you can simply iterate through
all nested values. After performing operation on values you revert dict to nested form.


# Instalation

You can copy functions directly into your code.

# Usage

`def example_nested_dict():
    return {'0-0':
                {'1-0':
                     {'2-0':
                          {'3-0': 'val',
                           '3-1': 'val'},
                      '2-1': {'3-0': ['val', 'val'],
                              '3-1': 'val'}},
                 '1-1': {'2-0': 'val'}},
            '0-1': 'val',
            '0-2': ['val', 'val']}`


`def example_flat_dict():
    return {'0-0:1-0:2-0:3-0': 'val',
            '0-0:1-0:2-0:3-1': 'val',
            '0-0:1-0:2-1:3-0': ['val', 'val'],
            '0-0:1-0:2-1:3-1': 'val',
            '0-0:1-1:2-0': 'val',
            '0-1': 'val',
            '0-2': ['val', 'val']}`

`# given
flat_dict = example_flat_dict()
# when
result_dict = flatten(nest(flat_dict))
# then
assert flat_dict == result_dict`
