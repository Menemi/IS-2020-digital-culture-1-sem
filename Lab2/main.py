import math
from PIL import Image

img = Image.open("image.jpg")
img = img.convert('L')
img.save("BW image.jpg")
line = []
pix = img.load()

for i in range(128):
    line.append(round(pix[64, i] // 20) * 20)
print("Mid line: ", line)
print()

frequency = {}
size = 0
for i in range(128):
    if line[i] in frequency:
        frequency[line[i]] += 1
    else:
        frequency[line[i]] = 1
        size += 1
print("Frequency list: ", frequency)
print()

sort_frequency = list(frequency.items())
sort_frequency.sort(key=lambda i: i[1])
print("Sorted frequency list: ", sort_frequency)
print()

length = math.ceil(math.log2(size))

color_frequency = []
for i in range(size):
    color_frequency.append(sort_frequency[i][1] / 128)

entropy = 0
for i in range(size):
    entropy += color_frequency[i] * math.log2(color_frequency[i])
entropy = -entropy
print("Number of alphabet characters: ", size)
print()
print("Minimum length of a bin code: ", length)
print()
print("Entropy: ", entropy)
print()

binary = []
for i in range(128):
    code = bin(line[i] // 20)[2:]
    if len(code) < 4:
        code = (4 - len(code)) * '0' + code
    binary.append(code)
print("Bin code: ", binary)
print()
print("Length of bin code: ", length * 128)
