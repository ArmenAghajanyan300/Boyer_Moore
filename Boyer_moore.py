def build_bad_character_table(pattern):
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char


def build_good_suffix_table(pattern):
    m = len(pattern)
    good_suffix = [0] * (m + 1)
    border = 0

    for i in range(m - 1, -1, -1):
        if pattern[i:] == pattern[:m - i]:
            border = m - i
        good_suffix[i] = border
    return good_suffix


def boyer_moore_search(text, pattern):
    
    bad_char = build_bad_character_table(pattern)
    good_suffix = build_good_suffix_table(pattern)

    matches = []
    m = len(pattern)
    n = len(text)
    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            matches.append(i)
            i += good_suffix[0] if 0 < good_suffix[0] < m else 1
        else:
            bad_char_shift = j - bad_char.get(text[i + j], -1)
            good_suffix_shift = good_suffix[j + 1] if j + 1 < len(good_suffix) else 1
            i += max(bad_char_shift, good_suffix_shift)

    return matches
