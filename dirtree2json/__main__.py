import argparse
import dirtree2json

parser = argparse.ArgumentParser()
parser.add_argument('src_dir', type=str)
parser.add_argument('-d', '--depth', type=int)
args = parser.parse_args()

if not args.depth:
    args.depth = 1

if not args.src_dir:
    print(dirtree2json().Tree(depth=args.depth))
else:
    print(dirtree2json().Tree(args.src_dir, depth=args.depth))
