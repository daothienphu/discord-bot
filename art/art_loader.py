import os
from typing import List
# from utils.composites import CompositeFile, CompositeFolder

ROOT_FOLDER = "art"

class ArtPathLoader():
    def __init__(self):
        self._currentFolderPath = ""
        # self._cacheFolderTree = CompositeFolder(ROOT_FOLDER, os.path.abspath(ROOT_FOLDER)) # TODO: Cache folders and files for faster lookup time.

    def LoadArtByNamesInFolder(self, folder: str, nameList: List[str]) -> List[str]:
        self._currentFolderPath = os.path.join(ROOT_FOLDER, folder)
        
        if not (os.path.exists(self._currentFolderPath) and os.path.isdir(self._currentFolderPath)):
            print(f"Folder path not found: {self._currentFolderPath}")
            return None
            
        # self._cacheFolderTree.AddToFolder(folder, self._currentFolderPath, True)
        return self.LoadArtByNames(nameList)
                
    def LoadArtByNames(self, nameList: List[str]) -> List[str]:
        pathList = []

        if not (os.path.exists(self._currentFolderPath) and os.path.isdir(self._currentFolderPath)):
            print(f"Current folder path is invalid: {self._currentFolderPath}")

        folderPathList = []
        for file in os.listdir(self._currentFolderPath):
            folderPathList.append(file)

        for name in nameList:
            for path in folderPathList:
                if path.startswith(name):
                    pathList.append(os.path.join(self._currentFolderPath, path))

        return pathList

def unitTest():
    artLoader = ArtPathLoader()
    for path in artLoader.LoadArtByNamesInFolder(folder="bonkCog", nameList=["bonk1", "bonk2", "bonk3", "bonk4", "bonk5"]):
        print(path)

if __name__ == "__main__":
    ROOT_FOLDER = "./"
    unitTest()