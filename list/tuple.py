"""
def main():
    coordinates = (42.376, -71.115) # that is the fixed location on earth by ensuring longitude and latitude. Therefore, we use the tuple.
    print(f"latitude: {coordinates[0]}")
    print(f"longitude: {coordinates[1]}")
main()
"""
#the trads-off tuple:
# 1. pros: it will save the memory. 
# 2. cons: it won't change and add any element into the tuple.
# Here i show u the details as below！
import sys

x = (12345,23456)
y = [12345, 23456]

print(f"{x} {sys.getsizeof(x)} bytes")
print(f"{y} {sys.getsizeof(y)} bytes")

x[0] = 1234
