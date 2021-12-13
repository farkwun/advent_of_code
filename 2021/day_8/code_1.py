from collections import namedtuple


Display = namedtuple("Display", "a b c d e f g")
Pattern = namedtuple("Pattern", "signals output mapping")
Translation = namedtuple("Translation", "displays")

SEV_SEG_0 = Display(1, 1, 1, 0, 1, 1, 1)
SEV_SEG_1 = Display(0, 0, 1, 0, 0, 1, 0)
SEV_SEG_2 = Display(1, 0, 1, 1, 1, 0, 1)
SEV_SEG_3 = Display(1, 0, 1, 1, 0, 1, 1)
SEV_SEG_4 = Display(0, 1, 1, 1, 0, 1, 0)
SEV_SEG_5 = Display(1, 1, 0, 1, 0, 1, 1)
SEV_SEG_6 = Display(1, 1, 0, 1, 1, 1, 1)
SEV_SEG_7 = Display(1, 0, 1, 0, 0, 1, 0)
SEV_SEG_8 = Display(1, 1, 1, 1, 1, 1, 1)
SEV_SEG_9 = Display(1, 1, 1, 1, 0, 1, 1)

A = "a"
B = "b"
C = "c"
D = "d"
E = "e"
F = "f"
G = "g"

CODE_TO_CHAR = {
    SEV_SEG_0: "0",
    SEV_SEG_1: "1",
    SEV_SEG_2: "2",
    SEV_SEG_3: "3",
    SEV_SEG_4: "4",
    SEV_SEG_5: "5",
    SEV_SEG_6: "6",
    SEV_SEG_7: "7",
    SEV_SEG_8: "8",
    SEV_SEG_9: "9",
}

FULLSET = {
    SEV_SEG_0,
    SEV_SEG_1,
    SEV_SEG_2,
    SEV_SEG_3,
    SEV_SEG_4,
    SEV_SEG_5,
    SEV_SEG_6,
    SEV_SEG_7,
    SEV_SEG_8,
    SEV_SEG_9,
}

CLEARSET = {
    # SEV_SEG_0,
    SEV_SEG_1,
    # SEV_SEG_2,
    # SEV_SEG_3,
    SEV_SEG_4,
    # SEV_SEG_5,
    # SEV_SEG_6,
    SEV_SEG_7,
    SEV_SEG_8,
    # SEV_SEG_9,
}


def generate_display_tuple(a=0, b=0, c=0, d=0, e=0, f=0, g=0):
    return Display(a, b, c, d, e, f, g)


def count_occurrences(character, signal_list):
    occurrences = 0
    for s in signal_list:
        if character in s:
            occurrences += 1
    return occurrences


def unmapped_chars(signal, mapping):
    return "".join(c for c in signal if c not in mapping)


def validate_mapping(pattern, mapping):
    signals = [pattern.signals] + [pattern.output]
    for s in signals:
        for code in s:
            new_code = [mapping[c] for c in code]
            dt = generate_display_tuple(**{c: 1 for c in new_code})
            if dt not in FULLSET:
                print("TRANSLATION ERROR")


def populate_mapping(pattern):
    mapping = {}
    signals = pattern.signals
    uniques = sorted([s for s in signals if len(s) in {2, 3, 4}], key=len)
    for p in uniques:
        if len(p) == 2:
            mapping[p[0]] = C if count_occurrences(p[0], signals) == 8 else F
            mapping[p[1]] = C if mapping[p[0]] != C else F
        if len(p) == 3:
            new_p = unmapped_chars(p, mapping)
            mapping[new_p[0]] = A
        if len(p) == 4:
            new_p = unmapped_chars(p, mapping)
            mapping[new_p[0]] = B if count_occurrences(new_p[0], signals) == 6 else D
            mapping[new_p[1]] = B if mapping[new_p[0]] != B else D
    len_6s = sorted(
        [s for s in signals if len(s) == 6],
        key=lambda s: len(unmapped_chars(s, mapping)),
    )
    mapping[unmapped_chars(len_6s[0], mapping)[0]] = G
    mapping[unmapped_chars(len_6s[1], mapping)[0]] = E
    # we can discard the last len_6 pattern - its either a 0 or a 6 -
    # in both cases we're looking for the same segment, E
    validate_mapping(pattern, mapping)
    return Pattern(signals, pattern.output, mapping)


def translate(pattern):
    _, output, mapping = pattern
    displays = []
    new_code = []
    for code in output:
        new_code = [mapping[c] for c in code]
        displays.append(generate_display_tuple(**{c: 1 for c in new_code}))
    return Translation(displays)


f = open("input.txt", "r")
# f = open("sample.txt", "r")
# f = [
#    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
# ]
patterns = []
for line in f:
    signals, output = line.rstrip().split("|")
    signals = tuple(signals.rstrip().split(" "))
    output = tuple([s for s in output.rstrip().split(" ") if s])

    patterns.append(Pattern(signals, output, {}))
f.close()


mappings = []
for p in patterns:
    mappings.append(populate_mapping(p))

translations = []
for m in mappings:
    translations.append(translate(m))

digit_counts = {}
for t in translations:
    for d in t.displays:
        if d not in digit_counts:
            digit_counts[d] = 0
        digit_counts[d] += 1

print(sum([count for digit, count in digit_counts.items() if digit in CLEARSET]))
