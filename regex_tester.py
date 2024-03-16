import regex as re

# I intentionally put it as list to see what the join method gives.
pattern = [r"1|"] + [r"2|"] + [r"12|"] + [r"3|"]
pattern = "".join(pattern)
pattern = pattern[:len(pattern)-1]
validation_pattern = f"[^{pattern}]"
input = "123$"
dict = {
    "1": ['A', 'B', 'C'],
    "2": ['D', 'E'],
    "12": ['X'],
    "3": ['P', 'Q']
}

matches_fa = re.findall(pattern, input, overlapped=True)
matches_fi = re.finditer(rf"(.*?<=({pattern}))", input, overlapped=True)
validation_fi =  re.finditer(rf"(?<=({validation_pattern}))", 
    input, overlapped=True)

list_matches_fi = [match.group(1) for match in matches_fi]
list_validation_fi = [match.group(1) for match in validation_fi]

print(pattern)
print(matches_fa)
print(list_matches_fi)
print(list_validation_fi)
print(list_validation_fi == [])

def findall_overlapped(pattern: str, input_string: str) -> list[str]:
    # Resulting list
    all_possible_substrings = []
    # Regex must match full string
    pattern = rf'^{pattern}$'
    # Iterate over all chars in a string
    for q in range(len(input_string)):
    # Iterate over the rest of the chars to the right
        for w in range(q,len(input_string)):  
            # Currently tested slice
            current_slice = input_string[q:w+1]
            # If there is a full slice match
            if re.match(pattern, current_slice):
                # Append it to the resulting list
                all_possible_substrings += [current_slice]
    result = []
    for key in dict.keys():
        if key in all_possible_substrings:
            result += [key]
    
    return result

result = findall_overlapped(pattern, input)
print(result)

