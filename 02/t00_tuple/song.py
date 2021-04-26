def song(verses, chorus):
    result = ()
    for v in verses:
        result += v
        result += chorus
    result += chorus
    return result
