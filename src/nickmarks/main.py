from argparse import ArgumentParser, Namespace
import sqlalchemy
import sys

def _parseargs() -> Namespace:
    parser = ArgumentParser()
    return parser.parse_args()

def main() -> int:
    args = _parseargs()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
