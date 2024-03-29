import timeit


def profile_flattening():

    instruction = """flatten(nested_dict)"""

    setup = """
from flat_nest_pydict import flatten;
from flat_nest_pydict import generate_nested_dict;
nested_dict = generate_nested_dict(6)"""

    t = timeit.Timer(instruction, setup)
    repeats = 1
    print('Flattening time: {}'.format(t.timeit(repeats)/repeats))


def profile_nesting():
    instruction = """nest(flat_dict)"""

    setup = """
from flat_nest_pydict import nest;
from flat_nest_pydict import generate_flat_dict;
flat_dict = generate_flat_dict(6)
"""

    t = timeit.Timer(instruction, setup)
    repeats = 1
    print('Nesting time: {}'.format(t.timeit(repeats)/repeats))

if __name__ == '__main__':
    profile_flattening()
    profile_nesting()

