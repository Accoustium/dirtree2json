import argparse
import dirtree2json

parser = argparse.ArgumentParser()
parser.add_argument('src_dir', type=str)
parser.add_argument('-d', '--depth', type=int)
args = parser.parse_args()

if not args.depth:
    args.depth = 1

if args.src_dir:
    t = dirtree2json.Tree(args.src_dir, depth=args.depth)
else:
    t = dirtree2json.Tree(depth=args.depth)

print(t)