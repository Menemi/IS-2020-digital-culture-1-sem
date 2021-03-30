import codecs


def editorialDistance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


with codecs.open("input.txt", encoding="utf-8") as f:
    text = f.read()

taskResults = open("taskResults.txt", "w")
correctText = text
# task_1_3
text = text.lower()

# task_1_2
for i in range(len(text) - 1, 0, -1):
    if text[i] == ".":
        text = text[:i] + "" + text[i + 1:]
    elif text[i] == "!":
        text = text[:i] + "" + text[i + 1:]
    elif text[i] == "?":
        text = text[:i] + "" + text[i + 1:]
    elif text[i] == ",":
        text = text[:i] + "" + text[i + 1:]
    elif text[i] == ";":
        text = text[:i] + "" + text[i + 1:]
    elif text[i] == ":":
        text = text[:i] + "" + text[i + 1:]
    elif text[i] == "«":
        text = text[:i] + "" + text[i + 1:]
    elif text[i] == "»":
        text = text[:i] + "" + text[i + 1:]
    elif text[i] == "(":
        text = text[:i] + "" + text[i + 1:]
    elif text[i] == ")":
        text = text[:i] + "" + text[i + 1:]
    elif text[i] == "—":
        text = text[:i] + "" + text[i + 1:]

# task_1_1
words = text.split()

task_2_1 = len(words)
print("task_2_1: ", file=taskResults)
print(task_2_1, file=taskResults)
print("", file=taskResults)

d = {}
for w in words:
    if d.get(w) is None:
        d[w] = 1
    else:
        d[w] += 1

counter_2_2 = 0
for i in d.values():
    counter_2_2 += 1

print("task_2_2: ", file=taskResults)
print(counter_2_2, file=taskResults)
print("", file=taskResults)

dict1 = {}
with codecs.open("dict1.txt", encoding="utf-8") as f:
    k = f.read().splitlines()
    for i in range(len(k)):
        dict1[k[i].split()[0]] = k[i].split()[1]

counter_2_3 = 0
not_included = []
right_words = []
for key1 in d.keys():
    included = False
    for key2 in dict1.keys():
        if key1 == key2:
            counter_2_3 += 1
            included = True
            break
    if not included:
        not_included.append(key1)

print("task_2_3: ", file=taskResults)
print(counter_2_3, file=taskResults)
print("", file=taskResults)

counter_3_1 = len(d.keys()) - counter_2_3
print("task_3_1: ", file=taskResults)
print(counter_3_1, file=taskResults)
print("", file=taskResults)

minimum = 100
for i in not_included:
    for j in dict1:
        if editorialDistance(i, j) < minimum:
            minimum = editorialDistance(i, j)
            index = j
    minimum = 100
    right_words.append(index)
    text = text.replace(i, index)
    correctText = correctText.replace(i, index)

print("task_3_2: ", file=taskResults)
for i in range(len(not_included)):
    print(not_included[i], " - ", editorialDistance(not_included[i], right_words[i]), file=taskResults)
print("", file=taskResults)

task_4_1 = len(text.split())
print("task_4_1: ", file=taskResults)
print(task_4_1, file=taskResults)
print("", file=taskResults)

dict2 = {}
for w in text.split():
    if dict2.get(w) is None:
        dict2[w] = 1
    else:
        dict2[w] += 1

task_4_2 = len(dict2.keys())
print("task_4_2: ", file=taskResults)
print(task_4_2, file=taskResults)
print("", file=taskResults)

task_4_3 = 0
for key1 in dict2.keys():
    for key2 in dict1.keys():
        if key1 == key2:
            task_4_3 += 1
            break

print("task_4_3: ", file=taskResults)
print(task_4_3, file=taskResults)
print("", file=taskResults)

print("task_5: ", file=taskResults)
for i in range(len(not_included)):
    print(not_included[i], " - ", right_words[i], " - ", editorialDistance(not_included[i], right_words[i]),
          file=taskResults)

with codecs.open("outText.txt", "w", encoding="utf-8") as f:
    f.write(correctText)
