import json

from PyQt5.QtXml import QDomElement

from AttrConditionData import AttrConditionData
from SmlAttributeTransfer import SmlAttributeTransfer

class SmlJsonAttrTransfer(SmlAttributeTransfer):
    def __init__(self):
        super(SmlJsonAttrTransfer, self).__init__()
        self.attrConditionData = AttrConditionData()

    def stringToJson(self, strData: str):
        return json.loads(str)

    def jsonToString(self):
        pass

    def changeAttrValue(self, docElement: QDomElement):
        pass