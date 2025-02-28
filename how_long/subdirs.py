import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--meoww", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.meoww:
    print("meow meow!")
