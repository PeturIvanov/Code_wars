unsigned_number = int(input())

IPv4 = [0, 0, 0, 0]

bits = []
while unsigned_number != 0:
    bit = unsigned_number % 2
    unsigned_number //= 2
    bits.append(str(bit))

bits = bits[::-1]

while len(bits) < 32:
    bits.insert(0, "0")

for i in range(len(IPv4)):
    IPv4[i] = ("".join(bits[0:8]))
    del bits[0:8]


for i, binary_num in enumerate(IPv4):
    result = 0
    degree = len(binary_num) - 1
    for num in binary_num:
        result += int(num) * 2 ** degree
        degree -= 1

    IPv4[i] = str(result)

IPv4 = ".".join(IPv4)
print(IPv4)
