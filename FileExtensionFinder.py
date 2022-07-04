import os
from typing import List


class FileExtensionFinder():
    def __init__(self):
        pass

    def fileExtensionCheck(self, fileName: str, extension: str):
        return fileName.endswith("." + extension)

    def allOfExtensionFilesFromDir(self, dir: str, filesRef: List[str], extension: str):
        for path in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, path)) and self.fileExtensionCheck(path, extension):
                filesRef.append(dir + '/' + path)
            elif os.path.isdir(os.path.join(dir, path)):
                self.allOfExtensionFilesFromDir(dir + '/' + path, filesRef, extension)

        return filesRef
