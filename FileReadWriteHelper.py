from Singleton import Singleton


class FileReadWriteHelper(metaclass=Singleton):
    def getFileContent(self, fileName: str):
        content = ''

        with open(fileName, "r", encoding='utf-8') as f:
            for lineText in f.readlines():
                content += lineText

        return content

    def reWriteFileContent(self, fileName: str, content: str):
        open(fileName, 'w').close()

        with open(fileName, "w", encoding='utf-8') as f:
            f.seek(0)
            f.truncate()
            f.write(content)
            f.close()