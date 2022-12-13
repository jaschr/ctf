#!/usr/bin/env python3

import base64

b64 = "anMvbXlmaWxlLnR4dA=="

decoded = base64.b64decode(b64)
print(decoded.decode('utf-8'))
