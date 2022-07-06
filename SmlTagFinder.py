from PyQt5.QtXml import QDomDocument, QDomElement

from AttrConditionData import AttrConditionData
from FileExtensionFinder import FileExtensionFinder
from FileReadWriteHelper import FileReadWriteHelper


class SmlTagFinder():
    def __init__(self, dirPath, tagName):
        self.fileExtensionFinder = FileExtensionFinder()
        self.dirPath = dirPath
        self.attrConditionData = AttrConditionData(tagName=tagName)

    def findAllOfSmlHasSpecificTag(self):

        retList = list()
        smlFileNames = list()
        self.fileExtensionFinder.allOfExtensionFilesFromDir(self.dirPath, smlFileNames, 'sml')

        for smlFileName in smlFileNames:
            content = FileReadWriteHelper().getFileContent(smlFileName)
            smlDoc = QDomDocument()
            smlDoc.setContent(content)

            if smlDoc.isNull():
                continue

            docElement = smlDoc.documentElement()
            # self.findAttr(docElement)
            if(self.hasTag(docElement)):
                retList.append(smlFileName)

        return retList

    def hasTag(self, element: QDomElement):
        tagNodes = element.elementsByTagName(self.attrConditionData.tagName)
        if(tagNodes.count() > 0):
            return True

        return False