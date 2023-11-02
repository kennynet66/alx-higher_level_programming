#!/usr/bin/python3
"""
    Calculates the sum of the arguments
"""
if __name__ == "__main__":
    import sys
    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
    print(f"{sum:d}")
