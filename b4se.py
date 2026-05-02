#!/usr/bin/env python3
"""b4se: encode and decode the boring stuff fast."""
import base64
import codecs
import sys

ENC = {
    "b64": lambda s: base64.b64encode(s.encode()).decode(),
    "b32": lambda s: base64.b32encode(s.encode()).decode(),
    "hex": lambda s: s.encode().hex(),
    "rot13": lambda s: codecs.encode(s, "rot13"),
    "bin": lambda s: " ".join(f"{b:08b}" for b in s.encode()),
}
DEC = {
    "b64": lambda s: base64.b64decode(s).decode(errors="replace"),
    "b32": lambda s: base64.b32decode(s).decode(errors="replace"),
    "hex": lambda s: bytes.fromhex(s).decode(errors="replace"),
    "rot13": lambda s: codecs.decode(s, "rot13"),
    "bin": lambda s: bytes(int(b, 2) for b in s.split()).decode(errors="replace"),
}

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("enc", "dec") or sys.argv[2] not in ENC:
        print("usage: b4se.py enc|dec b64|b32|hex|rot13|bin <text>")
        sys.exit(1)
    table = ENC if sys.argv[1] == "enc" else DEC
    print(table[sys.argv[2]](sys.argv[3]))
