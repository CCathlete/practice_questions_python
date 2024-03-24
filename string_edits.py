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
                return [source_slice[0]] + recursive_check(source_slice[1:], target_slice[1:])
# source_slice[0] != target_slice[0]
            result1 = recursive_check(source_slice[1:], target_slice) # skip s, delete s
            result2 = recursive_check(source_slice, target_slice[1:]) # skip t, add t
            if len(result1) <= len(result2):
                return ['-' + source_slice[0]] + result1
            else:
                return ['+' + target_slice[0]] + result2