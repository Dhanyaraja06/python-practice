def Sandwiched_Vowel(s):
    vowels = "aeiou"
    result = ""
    n = len(s)

    for i in range(n):
        if (s[i] in vowels) and (i > 0) and (i < n - 1) and (s[i-1] not in vowels) and (s[i+1] not in vowels):
            continue
        result += s[i]

    return result        
