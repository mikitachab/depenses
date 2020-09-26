from functools import reduce


def make_pipeline(funcs):
    def run(init_value=None):
        return reduce(lambda result, func: func(result), funcs, init_value)

    return run
