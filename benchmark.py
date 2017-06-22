import argparse
import json
import time


def timerfunc(func):
    def function_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print('The runtime for {} took {} seconds to \
                complete'.format(func.__name__, runtime))
        return value, runtime
    return function_timer


@timerfunc
def serialize_multiple(lines, sort=False):
    for obj in lines:
        json.dumps(obj, sort_keys=sort)


def main(args):
    with open(args.path) as f:
        objs_data = f.readlines()
    objs = [json.loads(line) for line in objs_data]
    print("Testing serialization of {} x {} element JSON \
            objects".format(len(objs), len(objs[0])))

    # fn = lambda l, s: serialize_multiple(l, s)
    results = {}
    for sort_val in (False, True):
        serialize_multiple(objs, sort_val)

    for k, v in results.items():
        print('{}, {}'.format(k, v))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run some JSON benchmarks')
    parser.add_argument('path',
                        type=str,
                        help='output filepath')

    args = parser.parse_args()
    main(args)
