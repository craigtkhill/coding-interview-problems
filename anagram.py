def is_anagram(s1,s2):
    s1_dict, s2_dict = convert_string_to_hash_table(s1), convert_string_to_hash_table(s2)
    return s1_dict == s2_dict

def convert_string_to_hash_table(string):
    hash_table = {}
    for char in string:
        char_lower = char.lower()
        if char_lower.isalpha():
            if char_lower in hash_table:
                hash_table[char_lower] += 1
            hash_table[char_lower] = 1
    return hash_table
        
s1 = "secure"
s2 = "rescue"
print(is_anagram(s1,s2))
