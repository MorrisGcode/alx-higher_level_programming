#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
     """Print all names in the hidden_4 module."""
 
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
