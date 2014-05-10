# coding: utf-8
from __future__ import print_function
from __future__ import unicode_literals


def gentest(f):
    limericks = list()
    with open(f) as f:
        for line in f:
            if len(line.strip()):
                limericks.append(line)

    return limericks





def main():
    # tests
    for l in gentest():
        print(l)


if __name__ == "__main__":
    main()
