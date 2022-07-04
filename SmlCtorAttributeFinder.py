from CtorArgsAttributeConditionData import CtorArgsAttributeConditionData
from SmlAttributeFinder import SmlAttributeFinder


class SmlCtorAttributeFinder(SmlAttributeFinder):
    def __init__(self, attrName, attrType, attrDefValue):
        super(SmlCtorAttributeFinder, self).__init__()
        self.attrConditionData = CtorArgsAttributeConditionData(attrName, attrType, attrDefValue)