"""
We need to make a tool that validate absolute direction rules.
Say we have a rule: A N B, that means that A is is_northern to B.
If we add the rule B N C, it also means that A is is_northern to C.
In that case, if we put in the rule C N A, it won't be valid and we need
to get a notice and not recieve the rule.
"""
import regex as re


class Point:

    def __init__(self, name: str) -> None:
        self.name = name
        self.is_northern_to: set[str] = set()
        self.is_eastern_to: set[str] = set()
        self.is_southern_to: set[str] = set()
        self.is_western_to: set[str] = set()


class LocationValidator:

    def __init__(self) -> None:
        self.points: dict[str,Point] = {}

    def check_rule_pattern(self, rule: str) -> None | list[str]:
        pattern = r'^(%w+) (%w+) (%w+)$'
        match = re.search(pattern, rule)
        if match:
            return [group for group in match.groups()]
        else:
            return None

    def get_relevant_point(self, point_name: str) -> Point:
        if point_name not in self.points.keys():
            self.points[point_name] = Point(point_name)
        return self.points[point_name]

    def set_rule(self, rule: str) -> None | str:
        return_value = self.check_rule_pattern(rule)
        if return_value:
            [name1, relative_direction, name2] = return_value
            point1 = self.get_relevant_point(name1)
            point2 = self.get_relevant_point(name2)
            
            match relative_direction.upper():
                case 'N':
                    # If point2 isn't already northern to point1 then
                    # point1 can be northern to point2.
                    if point1.name not in point2.is_northern_to:
                        point1.is_northern_to.update(point2.name, 
                                                  point2.is_northern_to)
                        point2.is_southern_to.update(point1.name, 
                                                 point1.is_southern_to)
                    else:
                        print('Rule is invalid. \n')
                
                case 'NE':
                    if point1.name not in point2.is_northern_to\
                    and point1.name not in point2.is_eastern_to:
                        
                        point1.is_northern_to.update(point2.name, 
                                                  point2.is_northern_to)
                        point2.is_southern_to.update(point1.name, 
                                                 point1.is_southern_to)
                        point1.is_eastern_to.update(point2.name, 
                                                  point2.is_eastern_to)
                        point2.is_western_to.update(point1.name, 
                                                 point1.is_western_to)
                    else:
                        print('Rule is invalid. \n')
                        
                case 'E':
                    if point1.name not in point2.is_eastern_to:
                        point1.is_eastern_to.update(point2.name, 
                                                  point2.is_eastern_to)
                        point2.is_western_to.update(point1.name, 
                                                 point1.is_western_to)
                    else:
                        print('Rule is invalid. \n')
                        
                case 'SE':
                    if point1.name not in point2.is_eastern_to\
                    and point1.name not in point2.is_southern_to:
                        
                        point1.is_southern_to.update(point2.name, 
                                                 point2.is_southern_to)
                        point2.is_northern_to.update(point1.name, 
                                                  point1.is_northern_to)
                        point1.is_eastern_to.update(point2.name, 
                                                  point2.is_eastern_to)
                        point2.is_western_to.update(point1.name, 
                                                 point1.is_western_to)
                    else:
                        print('Rule is invalid. \n')
                        
                case 'S':
                    if point1.name not in point2.is_southern_to:
                        point1.is_southern_to.update(point2.name, 
                                                  point2.is_southern_to)
                        point2.is_northern_to.update(point1.name, 
                                                 point1.is_northern_to)
                    else:
                        print('Rule is invalid. \n')
                        
                case 'SW':
                    if point1.name not in point2.is_western_to\
                    and point1.name not in point2.is_southern_to:
                        
                        point1.is_southern_to.update(point2.name, 
                                                 point2.is_southern_to)
                        point2.is_northern_to.update(point1.name, 
                                                  point1.is_northern_to)
                        point1.is_western_to.update(point2.name, 
                                                 point2.is_western_to)
                        point2.is_eastern_to.update(point1.name, 
                                                  point1.is_eastern_to)
                    else:
                        print('Rule is invalid. \n')
                        
                case 'W':
                    if point1.name not in point2.is_western_to:
                        point1.is_western_to.update(point2.name, 
                                                 point2.is_western_to)
                        point2.is_eastern_to.update(point1.name, 
                                                  point1.is_eastern_to)
                    else:
                        print('Rule is invalid. \n')
                        
                case 'NW':
                    if point1.name not in point2.is_northern_to\
                    and point1.name not in point2.is_southern_to:
                        
                        point1.is_northern_to.update(point2.name, 
                                                  point2.is_northern_to)
                        point2.is_southern_to.update(point1.name, 
                                                 point1.is_southern_to)
                        point1.is_western_to.update(point2.name, 
                                                 point2.is_western_to)
                        point2.is_eastern_to.update(point1.name, 
                                                  point1.is_eastern_to)
                    else:
                        print('Rule is invalid. \n')
                        


if __name__ == "__main__":
    pipi = LocationValidator()
    print(f"{globals()}\n\n\n{pipi.point[1]} and {pipi.point['hemlo']}")







