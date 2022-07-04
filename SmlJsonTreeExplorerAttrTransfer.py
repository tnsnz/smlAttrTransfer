import json
from typing import List, Dict

from PyQt5.QtXml import QDomElement

from SmlJsonAttrTransfer import SmlJsonAttrTransfer


class SmlJsonTreeExplorerAttrTransfer(SmlJsonAttrTransfer):
    def __init__(self, dirPath):
        super(SmlJsonTreeExplorerAttrTransfer, self).__init__()
        self.dirPath = dirPath
        self.attrConditionData.tagName = 'TreeExplorer'
        self.attrConditionData.attrName = 'treeRawJson'

    def changeAttrValue(self, docElement: QDomElement):
        tagNodes = docElement.elementsByTagName( self.attrConditionData.tagName)
        for i in range(len(tagNodes)):
            node = tagNodes.at(i)
            attrItem = node.attributes().namedItem(self.attrConditionData.attrName)
            changedData = self.changeJsonData(attrItem.nodeValue())
            attrItem.setNodeValue(json.dumps(changedData))

    def changeJsonData(self, jsonData):
        # for jsonStr in jsonList:
        becomeChangeData = json.loads(jsonData)
        self.findAndChangeJsonData(becomeChangeData)
        return becomeChangeData

    def findAndChangeJsonData(self, jsonData):
        if isinstance(jsonData, Dict):
            if 'str' == jsonData.get('type') and None != jsonData.get('value'):
                t = jsonData.get('value')
                jsonData['value'] = '\"' + t + '\"'
            for k, v in jsonData.items():
                self.findAndChangeJsonData(v)
        elif isinstance(jsonData, List):
            for json in jsonData:
                self.findAndChangeJsonData(json)

    def findAttr(self, element):
        ctorNodes = element.elementsByTagName(self.attrConditionData.tagName)
        result = []
        for i in range(len(ctorNodes)):
            node = ctorNodes.at(i)
            treeExplorerNode = node.attributes().namedItem(self.attrConditionData.attrName)

            if ('' != treeExplorerNode.nodeValue()):
                result.append(treeExplorerNode.nodeValue())

        return result