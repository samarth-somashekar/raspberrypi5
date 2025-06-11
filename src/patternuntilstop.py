import time
import sys

print("begin")
try:
    while True:
        size = 10

        for i in range(size):
            for j in range(size):
                dist = ((i - size//2)**2 + (j - size//2)**2)**0.5
                if abs(dist - size//2 + 1) < 1:
                    print(".", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(" " * ((size//2) * 2 - 1) + ".")
        
        sys.stdout.flush()  # Force immediate output
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nCaught KeyboardInterrupt")

print("end")
