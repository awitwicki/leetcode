def lengthOfLongestSubstring(s: str) -> int:
    max_count = 0
    if(len(s) == 1) : return 1

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 2):
            substr = s[i:j]
            substr_Set = set(s[i:j])
            s_len = len(set(s[i:j]))

            if s_len == j - i:
                max_count = max(max_count, len(substr_Set))
            else:
                break
            print(debug)
            debug = f'{i} {j} {substr} '
    return max_count

print(lengthOfLongestSubstring('abcabcbb')) #3
print(lengthOfLongestSubstring('bbb')) #1
print(lengthOfLongestSubstring('pwwkew')) #3
print(lengthOfLongestSubstring('')) #0
print(lengthOfLongestSubstring(' ')) #1
print(lengthOfLongestSubstring('vbxpvwkkteaiob')) #7
print(lengthOfLongestSubstring('xqgatvlevdqugapmlgymhkdgjthnqflpvtpqodujingqnvcyeamlmruvndkfivufokvcpqoxfunsrptvshhgzbcogotpknuyz')) #12
