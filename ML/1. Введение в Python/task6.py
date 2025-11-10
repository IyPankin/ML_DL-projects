def check(x: str, file: str):
    words = x.lower().split()
    dict = {}
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    with open(file, 'w') as f:
        for word in sorted(dict.keys()):
            f.write(f"{word} {dict[word]}\n")