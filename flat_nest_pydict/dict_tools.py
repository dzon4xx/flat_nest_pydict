from collections import Mapping


def flatten(nested_dict, sep=':'):
    """Returns flat dictionary. Returned dictionary has got number of leafs keys. Each of key is a path to leaf.

    example: nested_dict = {'0-0':
                                {'1-0': val
                                 '1-1': {'2-0': 'val'}},
                            '0-1': 'val',
                            '0-2': ['val', 'val']}

             flat = {'0-0:1-0': 'val',
                     '0-0:1-1:2-0': 'val',
                     '0-1': 'val',
                     '0-2': ['val', 'val']}"""

    def _flatten(nested_dict, flat_dict, aggregated_key):
        for current_key, current_val in nested_dict.items():
            if isinstance(current_val, Mapping):
                aggregated_key = sep.join([aggregated_key, current_key]) if aggregated_key else current_key
                aggregated_key = _flatten(current_val, flat_dict, aggregated_key)
            else:
                key = sep.join([aggregated_key, current_key]) if aggregated_key else current_key
                flat_dict[key] = current_val

        return sep.join(aggregated_key.split(sep)[:-1])  # return parent aggregated_key

    flat_dict = type(nested_dict)()
    _flatten(nested_dict, flat_dict, '')
    return flat_dict


def nest(flat_dict, sep=':'):
    """Returns nested dictionary. Flat dictionary must follow convention that each key is a path to nested leaf.

        example: nested_dict = {'0-0':
                                    {'1-0': val
                                     '1-1': {'2-0': 'val'}},
                                '0-1': 'val',
                                '0-2': ['val', 'val']}

                 flat = {'0-0:1-0': 'val',
                         '0-0:1-1:2-0': 'val',
                         '0-1': 'val',
                         '0-2': ['val', 'val']}"""

    def _nest(nested_dict, aggregated_key, val):
        try:
            leaf_key, aggregated_key = aggregated_key.split(sep, 1)
        except ValueError:
            leaf_key = aggregated_key
            dict_ = type(nested_dict)([(leaf_key, val)])
            nested_dict.update(dict_)
        else:
            if leaf_key not in nested_dict:
                nested_dict[leaf_key] = type(nested_dict)()
            _nest(nested_dict[leaf_key], aggregated_key, val)

    nested_dict = type(flat_dict)()
    for aggregated_key, val in flat_dict.items():
        _nest(nested_dict, aggregated_key, val)
    return nested_dict
