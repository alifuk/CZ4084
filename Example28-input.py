import sys
print(f"Spustili jste program s parametry {sys.argv[1]} a {sys.argv[2]}")
soucet = int(sys.argv[1]) + int(sys.argv[2])

print(f"Součet je: {soucet}")
print(type(sys.argv[1]))

