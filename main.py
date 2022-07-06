#for Example
'''
from EnvironVariable import getNativePath
from SmlCtorAttrTransfer import SmlCtorAttrTransfer

nativeSmlAttrTransfer = SmlCtorAttrTransfer("", "str", '""', getNativePath() + "/..", SmlCtorAttrTransfer.IgnoreAttr.IGNOREDNAME, True)
dispenserSmlAttrTransfer = SmlCtorAttrTransfer("", "str", '""', "C:/Users/soon/Desktop/Soon_dispenser_2021", SmlCtorAttrTransfer.IgnoreAttr.IGNOREDNAME, True)
laserSmlAttrTransfer = SmlCtorAttrTransfer("", "str", '""', "C:/Users/soon/Desktop/Soon_laser_cut_sorter", SmlCtorAttrTransfer.IgnoreAttr.IGNOREDNAME, True)

nativeSmlAttrTransfer.doRefactor()
dispenserSmlAttrTransfer.doRefactor()
laserSmlAttrTransfer.doRefactor()


from EnvironVariable import getNativePath
from SmlJsonTreeExplorerAttrTransfer import SmlJsonTreeExplorerAttrTransfer

dispensorTransfer = SmlJsonTreeExplorerAttrTransfer('C:/Users/soon/Desktop/Soon_dispenser_2021')
laserTransfer = SmlJsonTreeExplorerAttrTransfer("C:/Users/soon/Desktop/Soon_laser_cut_sorter")
frameworkTransfer = SmlJsonTreeExplorerAttrTransfer(getNativePath() + "/..")

dispensorTransfer.doRefactor()
laserTransfer.doRefactor()
frameworkTransfer.doRefactor()


from SmlTagFinder import SmlTagFinder

a = SmlTagFinder('C:/Users/soon/Desktop/Soon_dispenser_2021', 'TreeExplorer')
r = a.findAllOfSmlHasSpecificTag()

from EnvironVariable import getNativePath

from SmlTagFinder import SmlTagFinder

smlTagFinder = SmlTagFinder('C:/Users/soon/Desktop/Soon_dispenser_2021', 'TreeExplorer')
smlTagFinder2 = SmlTagFinder(getNativePath() + "/..", 'TreeExplorer')
hasTagSmls = smlTagFinder.findAllOfSmlHasSpecificTag()
hasTagSmls2 = smlTagFinder2.findAllOfSmlHasSpecificTag()
'''