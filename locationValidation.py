"""
We need to make a tool that validate absolute direction rules.
Say we have a rule: A N B, that means that A is northern to B.
If we add the rule B N C, it also means that A is northern to C.
In that case, if we put in the rule C N A, it won't be valid and we need
to get a notice and not recieve the rule.
"""
import regex as re

class Point:
    def __init__(self, name: str) -> None:
        self.name = name
        self.northern_to = ''
        self.eastern_to = ''
        self.southern_to = ''
        self.western_to = ''

def validate_rule(rule: str) -> None | list[str]:
    pattern = r'^(%w+) (%w+) (%w+)$'
    match = re.search(pattern, rule)
    if match:
        return [group for group in match.groups()]
    else:
        return None


