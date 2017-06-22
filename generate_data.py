import argparse
import json
import random


def serialize(item, sort=False):
    json.dumps(item, sort=sort)


def main(args):
    word_file = "/usr/share/dict/words"
    WORDS = open(word_file).read().splitlines()
    num_words = len(WORDS)

    with open(args.path, 'w') as out_file:
        for i in range(0, args.objects):
            data = {}
            while len(data) < args.elements:
                key = WORDS[random.randint(0, num_words)]
                if key not in data:
                    data[key] = random.random()
            json.dump(data, out_file)
            out_file.write("\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run some JSON benchmarks')
    parser.add_argument('elements',
                        type=int,
                        help='Number of elements per JSON object')
    parser.add_argument('objects',
                        type=int,
                        help='Number of JSON objects')
    parser.add_argument('path',
                        type=str,
                        help='output filepath')

    args = parser.parse_args()
    main(args)
