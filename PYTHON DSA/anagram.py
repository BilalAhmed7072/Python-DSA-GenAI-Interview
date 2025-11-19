def is_anagram(a,b):
    """this functon will check these strings are anagram are not"""
    if len(a) != len(b):
        return False
    
    count = {}
    for ch in a:
        count[ch] = count.get(ch, 0) +1

    for ch in b:
        if ch not in count:
            return False
        count[ch] -=1
        if count[ch]==0:
            del count[ch]
    return len(count) ==0