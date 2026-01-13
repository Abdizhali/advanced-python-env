with open("text.txt", "r") as f:
    lines = f.readlines()

words = []
for line in lines:
    line = line.lower()
    for ch in ".,!?":
        line = line.replace(ch, "")
    words += line.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

with open("analysis.txt", "w") as f:
    f.write("Lines: " + str(len(lines)) + "\n")
    f.write("Words: " + str(len(words)) + "\n")
    for w in freq:
        f.write(w + " " + str(freq[w]) + "\n")
