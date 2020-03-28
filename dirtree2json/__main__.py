import argparse
from dirtree2json import Tree

parser = argparse.ArgumentParser()
parser.add_argument('--src_dir', type=str)
parser.add_argument('-d', '--depth', type=int)
args = parser.parse_args()


if args.depth is None:
    args.depth = 1

if not args.src_dir:
    t = Tree(depth=args.depth)
    print(t.display)
else:
    t = Tree(args.src_dir, depth=args.depth)
    print(t.display)
