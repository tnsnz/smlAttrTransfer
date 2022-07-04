from PyQt5.QtCore import QByteArray, QXmlStreamWriter
from PyQt5.QtXml import QDomDocument

from FileExtensionFinder import FileExtensionFinder
from FileReadWriteHelper import FileReadWriteHelper


class SmlAttributeTransfer():
    def __init__(self):
        self.attrConditionData = None
        self.dirPath = ''
        self.fileExtensionFinder = FileExtensionFinder()

    def setAttrName(self, attrName):
        self.attrConditionData.attrName = attrName

    def setAttrType(self, attrType):
        self.attrConditionData.attrType = attrType

    def setAttrDefValue(self, attrDefValue):
        self.attrConditionData.attrType = attrDefValue

    def doRefactor(self):
        smlFileNames = list()
        self.fileExtensionFinder.allOfExtensionFilesFromDir(self.dirPath, smlFileNames, 'sml')

        for smlFileName in smlFileNames:
            content = FileReadWriteHelper().getFileContent(smlFileName)
            smlDoc = QDomDocument()
            smlDoc.setContent(content)

            if smlDoc.isNull():
                continue

            docElement = smlDoc.documentElement()
            self.changeAttrValue(docElement)

            qBytes = QByteArray()
            xmlWriter = QXmlStreamWriter(qBytes)

            xmlWriter.writeStartDocument()
            xmlWriter.setAutoFormatting(True)
            self.reWriteChildNode(xmlWriter, docElement)
            xmlWriter.writeEndDocument()

            FileReadWriteHelper().reWriteFileContent(smlFileName, str(qBytes, 'utf-8'))

    def reWriteChildNode(self, xmlWriter, element):
        attributeList = element.attributes()
        attributes = []
        xmlWriter.writeStartElement(element.nodeName())

        for idx in range(len(attributeList)):
            attributes.append(attributeList.item(idx))

        attributes.sort(key=lambda x: x.nodeName())

        for attr in attributes:
            xmlWriter.writeAttribute(attr.nodeName(), attr.nodeValue())

        if not element.firstChild().isNull():
            self.reWriteChildNode(xmlWriter, element.firstChild().toElement())

        xmlWriter.writeEndElement()

        if not element.nextSibling().isNull():
            self.reWriteChildNode(xmlWriter, element.nextSibling().toElement())

    def changeAttrValue(self, docElement):
        pass