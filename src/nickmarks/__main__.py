#!/bin/env python
import sys

from .cli import parse_args
from .nickmarks import main

sys.exit(main(parse_args()))
