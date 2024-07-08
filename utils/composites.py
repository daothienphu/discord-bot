class CompositeObject:
    def __init__(self, name: str, path: str) -> None:
        self.Name = name
        self.Path = path

class CompositeFolder(CompositeObject):
    def __init__(self, name, path) -> None:
        super().__init__(name, path)
        self.Folder = []

    def AddToFolder(self, name: str, path: str, isFolder: bool) -> None:
        compositeObject = None
        if (isFolder):
            compositeObject = CompositeFolder(name, path)
        else:
            compositeObject = CompositeFile(name, path)

        self.AddObjectToFolder(compositeObject)

    def AddObjectToFolder(self, item: CompositeObject) -> None:
        self.Folder.append(item)

class CompositeFile(CompositeObject):
    def __init__(self, name: str, path: str) -> None:
        super().__init__(name, path)