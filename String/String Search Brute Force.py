def brute_force_string_search(text, pattern):
    m = len(pattern)
    n = len(text)
    indices = []
    
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            indices.append(i)
    
    return indices

text = "ABABDABACDABABCABAB"
pattern = "ABAB"

result = brute_force_string_search(text, pattern)

print("Pattern found at indices:", result)