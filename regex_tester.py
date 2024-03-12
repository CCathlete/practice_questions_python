import regex as re

pattern = [r"1|"] + [r"12|"] + [r"3|"]
pattern = "".join(pattern)
pattern = pattern[:len(pattern)-1]
validation_pattern = f"[^{pattern}]"
input = "123$"

matches_fa = re.findall(rf"(?<={pattern})", input, overlapped=True)
matches_fi = re.finditer(rf"(?<=({pattern}))", input, overlapped=True)
validation_fi =  re.finditer(rf"(?<=({validation_pattern}))", 
                             input, overlapped=True)

list_matches_fi = [match.group(1) for match in matches_fi]
list_validation_fi = [match.group(1) for match in validation_fi]

print(pattern)
print(matches_fa)
print(list_matches_fi)
print(list_validation_fi)
print(list_validation_fi == [])