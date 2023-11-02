#!/usr/bin/python3
"""
    Prints the arguements received
"""
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print(f"{length} arguments:")
    for i in range(length):
        print(f"{i + 1}: {sys.argv[i + 1]}")