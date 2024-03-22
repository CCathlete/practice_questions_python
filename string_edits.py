class StrEditor:
    def __init__(self, source: str, target: str) -> None:
        self.source = source
        self.target = target

    def count_edits(self) -> list[str]:
        source = self.source
        target = self.target
          def recursive_check(source_slice: str, target_slice: str) -> list[str]:
              