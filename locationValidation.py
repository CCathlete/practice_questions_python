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
        self.northern_to: set[str] = set()
        self.eastern_to: set[str] = set()
        self.southern_to: set[str] = set()
        self.western_to: set[str] = set()


class LocationValidator:

    def check_rule_pattern(self, rule: str) -> None | list[str]:
        pattern = r'^(%w+) (%w+) (%w+)$'
        match = re.search(pattern, rule)
        if match:
            return [group for group in match.groups()]
        else:
            return None

    def set_rule(self, rule: str) -> None | str:
        return_value = self.check_rule_pattern(rule)
        if return_value:
            [name1, relative_direction, name2] = return_value
            point1, point2 = Point(name1), Point(name2)
            match relative_direction:
                case 'N' | 'n':
                    # If point2 isn't already northern to point1 then
                    # point1 can be northern to point2.
                    if point1.name not in point2.northern_to:
                        point1.northern_to += [point2.name]
                        point2.southern_to += [point1.name]
                    else:
                        print('Rule is invalid. \n')
                case 'NE' | 'ne':
                    if point1.name not in point2.northern_to\
                    and point1.name not in point2.eastern_to:
                        point1.northern_to += [point2.name]
                        point1.eastern_to += [point2.name]
                        point2.southern_to += [point1.name]
                        point2.western_to += [point1.name]
                    else:
                        print('Rule is invalid. \n')
                case 'E' | 'e':
                    point1.eastern_to = point2.name
                case 'SE' | 'se':
                    point1.southern_to = point2.name
                    point1.eastern_to = point2.name
                case 'S' | 's':
                    point1.southern_to = point2.name
                case 'SW' | 'sw':
                    point1.southern_to = point2.name
                    point1.western_to = point2.name
                case 'W' | 'w':
                    point1.western_to = point2.name
                case 'NW' | 'nw':
                    point1.northern_to = point2.name
                    point1.western_to = point2.name
