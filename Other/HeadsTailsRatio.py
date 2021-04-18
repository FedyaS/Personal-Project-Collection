sequence = "ttthhtttth"
sequence = sequence.lower()

highest_ratio = 0

for s1 in range(len(sequence)):
    for s2 in range(s1 + 1, len(sequence)):
        sub = sequence[s1:s2+1]
        hs = 0
        ts = 0
        higher_ratio = 0
        for c in sub:
            if c == 'h':
                hs += 1
            elif c == 't':
                ts += 1

        if hs == 0 or ts == 0:
            higher_ratio = 0
        else:
            if hs > ts:
                higher_ratio = hs / (hs + ts)
            else:
                higher_ratio = ts / (hs + ts)

        if higher_ratio > highest_ratio:
            highest_ratio = higher_ratio


print(highest_ratio)