

class NameFormatter():
    def FormatName(self, name: str) -> str:
        return name.replace('_', '').strip().lower()
