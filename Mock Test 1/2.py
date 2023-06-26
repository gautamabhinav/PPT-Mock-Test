def firstUniqChar(s):
    
    char_count = {} 

    # Count the frequency of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the index of the first non-repeating character
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1  # No non-repeating character found


s = "leetcode"
print(firstUniqChar(s))  

s = "loveleetcode"
print(firstUniqChar(s)) 

s = "aabb"
print(firstUniqChar(s))  
