from PyQt5.QtXml import QDomElement

from CtorArgsAttributeConditionData import CtorArgsAttributeConditionData
from SmlAttributeTransfer import SmlAttributeTransfer


class SmlCtorAttrTransfer(SmlAttributeTransfer):
    class IgnoreAttr:
        NOTIGNORE = 0b0000
        IGNOREDNAME = 0b0001
        IGNOREDTYPE = 0b0010
        IGNOREDVALUE = 0b0100

    def __init__(self, attrName, attrType, attrDefValue, dirPath, ignore: IgnoreAttr = IgnoreAttr.NOTIGNORE, upathRename = False):
        super(SmlCtorAttrTransfer, self).__init__()
        self.attrConditionData = CtorArgsAttributeConditionData(attrName, attrType, attrDefValue)
        self.dirPath = dirPath
        self.ignoreFlag = ignore
        self.upathRenameFlag = upathRename

    def changeAttrValue(self, element: QDomElement):
        if (None == element):
            return

        ctorNodes = element.elementsByTagName(self.attrConditionData.tagName)

        assert (None != ctorNodes)

        for i in range(len(ctorNodes)):
            ctorNode = ctorNodes.at(i)
            defValElement = ctorNode.attributes().namedItem('defval')
            nameElement = ctorNode.attributes().namedItem('name')
            typeElement = ctorNode.attributes().namedItem('type')

            if not self.ignoreFlag & self.IgnoreAttr.IGNOREDVALUE and "" == defValElement.nodeValue():
                ctorNode.toElement().setAttribute('defval', self.attrConditionData.attrDefValue)

            if not self.ignoreFlag & self.IgnoreAttr.IGNOREDVALUE and "" == nameElement.nodeValue():
                ctorNode.toElement().setAttribute('name', self.attrConditionData.attrName)

            if not self.ignoreFlag & self.IgnoreAttr.IGNOREDVALUE and "" == typeElement.nodeValue():
                ctorNode.toElement().setAttribute('type', self.attrConditionData.attrType)

            if self.upathRenameFlag and "upath" == nameElement.nodeValue() and not defValElement.nodeValue().startswith('"') and '' != defValElement.nodeValue():
                ctorNode.toElement().setAttribute('defval', '"' + defValElement.nodeValue() + '"')
                pass

    def setIgnoreFloag(self, flag):
        self.ignoreFlag = flag