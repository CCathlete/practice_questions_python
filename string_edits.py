class StrEditor:
    def __init__(self, source: str, target: str) -> None:
        self.source = source
        self.target = target

    def count_edits(self) -> list[str]:
        source = self.source
        target = self.target
        def recursive_check(source_slice: str, target_slice: str) -> list[str]:
            if len(target_slice) == 0 and len(source_slice) > 0:
                return ['-' + char for char in source_slice]
            elif len(target_slice) > 0 and len(source_slice) == 0:
                return ['+' + char for char in target_slice]
            elif len(target_slice) == 0 and len(source_slice) == 0:
                return []
            if source_slice[0] == target_slice[0]:
                return [source_slice[0]] + recursive_check(
                    source_slice[1:], target_slice[1:])
# source_slice[0] != target_slice[0]
# skip s, delete s
            result1 = recursive_check(source_slice[1:], target_slice) 
# skip t, add t
            result2 = recursive_check(source_slice, target_slice[1:]) 
            if len(result1) <= len(result2):
                return ['-' + source_slice[0]] + result1
            else:
                return ['+' + target_slice[0]] + result2
        return recursive_check(source, target)

    def fuck_the_recursive_way(self) -> list[str]:
        source = self.source
        target = self.target
        result = []
        for target_char in target:
            didnt_find_in_source = True
            for i, source_char in enumerate(source):
                if target_char == source_char:
                    result += [target_char]
                    if i > 0:
                        source = source[:i] + source[i+1:]
                    else:
                        source = source[i+1:]
                    # We found in source so:
                    didnt_find_in_source = False
                    break

            if didnt_find_in_source:
                result += [f'+{target_char}']

        for whats_letf in source:
            result += [f'-{whats_letf}']

        return result


def main() -> None:
    source = 'ABCAAJJK'
    target = 'KAAJBAF'
    my_editor = StrEditor(source, target)

    print(f"The recursive solution: {my_editor.count_edits()}\n")
    print(f"The o(n^2) solution: {my_editor.fuck_the_recursive_way()}\n")

    
if __name__ == '__main__':
    main()