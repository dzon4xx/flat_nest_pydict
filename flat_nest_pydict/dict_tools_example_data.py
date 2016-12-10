from .dict_tools import flatten


def example_nested_dict():
    return {'0-0':
                {'1-0':
                     {'2-0':
                          {'3-0': 'val',
                           '3-1': 'val'},
                      '2-1': {'3-0': ['val', 'val'],
                              '3-1': 'val'}},
                 '1-1': {'2-0': 'val'}},
            '0-1': 'val',
            '0-2': ['val', 'val']}


def example_flat_dict():
    return {'0-0:1-0:2-0:3-0': 'val',
            '0-0:1-0:2-0:3-1': 'val',
            '0-0:1-0:2-1:3-0': ['val', 'val'],
            '0-0:1-0:2-1:3-1': 'val',
            '0-0:1-1:2-0': 'val',
            '0-1': 'val',
            '0-2': ['val', 'val']}


def generate_nested_dict(num_of_levels):

    def _generate(level, leaf_number, dict_):
        if level == num_of_levels:
            key = '-'.join([str(level), str(leaf_number)])
            dict_.update({key: 'val'})

        else:
            for leaf_number in range((level+1)*2):
                key = '-'.join([str(level), str(leaf_number)])
                child_dict = {}
                _generate(level+1, leaf_number, child_dict)
                dict_.update({key: child_dict})

    dict_ = {}
    _generate(0, 0, dict_)
    return dict_

def generate_flat_dict(num_of_levels):

    def _generate(level, leaf_number, dict_):
        if level == num_of_levels:
            key = '-'.join([str(level), str(leaf_number)])
            dict_.update({key: 'val'})

        else:
            for leaf_number in range((level+1)*2):
                key = '-'.join([str(level), str(leaf_number)])
                child_dict = {}
                _generate(level+1, leaf_number, child_dict)
                dict_.update({key: child_dict})

    dict_ = {}
    _generate(0, 0, dict_)
    flat_dict = flatten(dict_)
    return flat_dict