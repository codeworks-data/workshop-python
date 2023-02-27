def findWord(iterable):
    d = dict(
        rule.split('>') for rule in iterable
    )
    letters_without_parent = set(d.keys()) - set(d.values())

    if len(letters_without_parent) != 1:
        raise ValueError
        
    current = letters_without_parent.pop()
    result = current
    while True:
        try:
            current = d[current]
            result += current
        except KeyError:
            return result