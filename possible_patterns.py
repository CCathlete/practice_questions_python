"""### QUESTION
Given a string as input, return the list of all the possible patterns:

```
{ "1" : ['A', 'B', 'C'],
"2" : ['D', 'E'],
"12" : ['X'],
"3" : ['P', 'Q'] }
```

Example if input is "123", then output is ["ADP","ADQ","AEP","AEQ",
"BDP","BDQ","BEP","BEQ","CDP","CDQ","CEP","CEQ","XP","XQ"]

Assume, you must match the input entirely in-order to produce an output.

### EXPLANATION
This is from a facebook phone screen.
Your ability to understand how recursion and how the stack relate will 
greatly help in solving this problem. There are two issues to point out. 
First issue is the string pattern matching  of the input '123' to the 
dictionary. Then there is the possible patterns problem after you have 
accessed a list and started to create your result.

The first issue is fairly easy. You should have a known start and end 
index in the string, use these indexes to create a sub-string then try 
to match that to the dictionary, if not, increment the end index once 
and try again.

For the second issue, this is when you have to think about how you are 
going to store your answer. First, we know we have to use recursion for 
each element in the list. But the next new recursion you call, it must 
be provided the currently built result so far. Your base case is when 
you have reached the last index of the string AND the first issue is 
resolved. Then and only then should you add your current result to the 
final result. 

What happens if you reached the end of the index but the first issue 
isn't resolved? You get a string that doesn't exist in the dictionary? 
Then you must retrace your steps and remove the last item you placed in 
your result. This is when you will realize a stack is the most 
appropriate method to save your current result. As you move forward, 
you add to the stack. If you reach a dead end, then go back and pop off 
the last item in your stack and try another element, push that on the 
stack. Repeat until you reached the end of the index, then add all the 
contents in the stack to your result. Continue to back-track, pop off 
and find other possibilities.
"""
"""### BRUTE FORCE SOLUTION
```
def get_possible_patterns(string, dictionary, stack):
results = list()
# is the substring in the dictionary?
for index in range(0, len(string)+1):
    substring = string[0:index+1]
    if substring in dictionary:
        # yes, add an element from list and call recursion
        for element in dictionary[substring]:
            stack.append(element)
            # are we at end?
            if index == len(string)-1:
                results.append(''.join(stack))
            else:
                new_string = string[index+1:]
                results_found = get_possible_patterns(
                                    new_string, 
                                    dictionary, 
                                    stack)
                # Reach a dead end
                # For the scenario that a list has a majority of the values 
                # but can never exactly match the string
                if len(results_found) == 0:
                    stack.pop()
                    break
                results += results_found
            stack.pop()
return results


dictionary = { "1" : ['A', 'B', 'C'],
            "2" : ['D', 'E'],
            "12" : ['X'],
            "3" : ['P', 'Q'] }

string = '123'
stack = list()
print get_possible_patterns(string, dictionary, stack)
```
"""
from collections.abc import Iterator
import regex as re


class pattern_finder:

    def __init__(self, pattern_dict: dict[str, list[str]], input: str) -> None:
        self.pattern_dict = pattern_dict
        self.input = input

    def pattern_from_keys(self) -> str:
        # Creating a search pattern for regex from the keys of
        # our dictionary.
        regex_search_pattern = [rf"{key}|" for key in self.pattern_dict.keys()]
        regex_search_pattern = "".join(regex_search_pattern)
        # Removing the last "|" from the string we created, creating
        # a regex pattern of the form key1|key2|...|key N.
        regex_search_pattern =\
         regex_search_pattern[:len(regex_search_pattern)-1]

        return regex_search_pattern

    def validate_input(self) -> None:
        # Creating a search pattern of the form [^key1|..|key N]
        # to find expressions that does not appear in our keys list.
        validation_pattern = "[^" + self.pattern_from_keys() + "]"
        unwanted_expressions = re.finditer(rf"(?<=({validation_pattern}))",
                                           self.input,
                                           overlapped=True)
        list_validation = [match.group(1) for match in unwanted_expressions]
        assert (list_validation == [])

    def dig_in(self, matches_iterator: Iterator[str]) -> list[str]:
        # When the next value is the end string we've already saved
        # the last real value in out previous call.
        key_match = next(matches_iterator, "end of keys")
        if key_match == "end of keys":
            return [""]
        else:
            return_list = []
            for pattern in self.pattern_dict[key_match]:
                return_list +=\
                list(map(lambda x:pattern + x, self.dig_in(matches_iterator)))
            return return_list

    def find_patterns(self) -> list[str]:
        # Validating that there are no characters in our input that
        # are not in our keys list.
        self.validate_input()
        regex_search_pattern = self.pattern_from_keys()
        # Finding all variations of the dict's keys in out input string.
        # Note: this is an iterator of match objects.
        matches_of_keys_iterator = re.finditer(
            rf"(?<=({regex_search_pattern}))", self.input, overlapped=True)
        matches_of_keys_list = [
            match.group(1) for match in matches_of_keys_iterator
        ]
        # Converting the list into an iterator of strings.
        match_to_string_iterator = iter(matches_of_keys_list)
        results = self.dig_in(match_to_string_iterator)
        return results


def main() -> None:
    input = "123"
    dict = {
        "1": ['A', 'B', 'C'],
        "2": ['D', 'E'],
        "12": ['X'],
        "3": ['P', 'Q']
    }
    my_pattern_finder = pattern_finder(dict, input)
    results = my_pattern_finder.find_patterns()
    print(results)
