f = open("input.txt", "r")
diagnostics = []
for line in f:
    diagnostics.append(line.rstrip())
f.close()

# diagnostics = [
#    "00100",
#    "11110",
#    "10110",
#    "10111",
#    "10101",
#    "01111",
#    "00111",
#    "11100",
#    "10000",
#    "11001",
#    "00010",
#    "01010",
# ]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.counts = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_string(self, string):
        node = self.root
        for c in string:
            if c not in node.children:
                node.children[c] = TrieNode()
            if c not in node.counts:
                node.counts[c] = 0
            node.counts[c] += 1
            node = node.children[c]


trie = Trie()

for d in diagnostics:
    trie.add_string(d)

# find oxy
oxy = []
node = trie.root
while node.children:
    if len(node.children) == 1:
        for key, val in node.children.items():
            oxy.append(str(key))
            node = node.children[key]
        continue
    if node.counts.get("1", 0) < node.counts.get("0", 0):
        oxy.append("0")
        node = node.children["0"]
    else:
        oxy.append("1")
        node = node.children["1"]

# find co2
co2 = []
node = trie.root
while node.children:
    if len(node.children) == 1:
        for key, val in node.children.items():
            co2.append(str(key))
            node = node.children[key]
        continue
    if node.counts.get("1", 0) < node.counts.get("0", 0):
        co2.append("1")
        node = node.children["1"]
    else:
        co2.append("0")
        node = node.children["0"]

oxy = "".join(oxy)
co2 = "".join(co2)

oxy = int(oxy, 2)
co2 = int(co2, 2)

print(oxy, co2)
print(oxy * co2)
