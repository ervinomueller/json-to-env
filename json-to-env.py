#!/usr/bin/env python

import json
import pipes
import argparse

parser = argparse.ArgumentParser(description='json load and print')
parser.add_argument('-i','--inputstring', help='Input String in JSON format', required=True)

args = parser.parse_args()
inp = args.inputstring

for k, v in json.loads(inp).items():
    k = pipes.quote(k)
    v = pipes.quote(v)
    print("%s=%s" % (k, v))