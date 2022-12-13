#!/usr/bin/env python
import base64
encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"
decodedkey = base64.b64decode(encodedkey)
print("picoCTF{" + decodedkey.decode('utf-8') + "}")

