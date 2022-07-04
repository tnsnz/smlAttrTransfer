from AttrConditionData import AttrConditionData


class CtorArgsAttributeConditionData(AttrConditionData):
    def __init__(self, attrName="", attrType="", attrDefValue=""):
        super(CtorArgsAttributeConditionData, self).__init__(attrName, attrType, attrDefValue, 'CtorArg')