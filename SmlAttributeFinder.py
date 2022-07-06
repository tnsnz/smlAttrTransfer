from PyQt5.QtXml import QDomDocument, QDomElement

from AttrConditionData import AttrConditionData
from FileExtensionFinder import FileExtensionFinder
from FileReadWriteHelper import FileReadWriteHelper


class SmlAttributeFinder():
    def __init__(self, dirPath, tagName, attrName):
        self.fileExtensionFinder = FileExtensionFinder()
        self.dirPath = dirPath
        self.attrConditionData = AttrConditionData(attrName=attrName, tagName=tagName)

    def findAllOfSmlHasSpecificAttr(self):

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
            if(self.hasAttr(docElement)):
                retList.append(smlFileName)

        return retList

    def findAttr(self, element: QDomElement):
        ctorNodes = element.elementsByTagName(self.attrConditionData.tagName)
        result = []
        for i in range(len(ctorNodes)):
            node = ctorNodes.at(i)
            treeExplorerNode = node.attributes().namedItem(self.attrConditionData.attrName)
            result.append(treeExplorerNode.nodeValue())

        return result

    def hasAttr(self, element: QDomElement):
        ctorNodes = element.elementsByTagName(self.attrConditionData.tagName)
        result = False
        for i in range(len(ctorNodes)):
            node = ctorNodes.at(i)
            treeExplorerNode = node.attributes().namedItem(self.attrConditionData.attrName)
            if(not treeExplorerNode.isNull()):
                result = True
                break

        return result