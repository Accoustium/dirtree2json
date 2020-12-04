import argparse
from dirtree2json import Tree

parser = argparse.ArgumentParser()
parser.add_argument("--src_dir", type=str)
parser.add_argument("-d", "--depth", type=int)
parser.add_argument("-f", "--filler", type=str)
args = parser.parse_args()


if args.depth is None:
    args.depth = 1

if args.filler is None:
    args.depth = "  "

if not args.src_dir:
    t = Tree(depth=args.depth, filler=args.filler)
    print(t.display)
else:
    t = Tree(args.src_dir, depth=args.depth, filler=args.filler)
    print(t.display)
