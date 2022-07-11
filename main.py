#for Example
'''
from EnvironVariable import getNativePath
from SmlCtorAttrTransfer import SmlCtorAttrTransfer

nativeSmlAttrTransfer = SmlCtorAttrTransfer("", "str", '""', getNativePath() + "/..", SmlCtorAttrTransfer.IgnoreAttr.IGNOREDTYPE | SmlCtorAttrTransfer.IgnoreAttr.IGNOREDNAME, True)
nativeSmlAttrTransfer.doRefactor()

dispenserSmlAttrTransfer = SmlCtorAttrTransfer("", "str", '""', "C:/Users/soon/Desktop/Soon_dispenser_2021", SmlCtorAttrTransfer.IgnoreAttr.IGNOREDTYPE | SmlCtorAttrTransfer.IgnoreAttr.IGNOREDNAME, True)
dispenserSmlAttrTransfer.doRefactor()

# skip
# laserSmlAttrTransfer = SmlCtorAttrTransfer("", "str", '""', "C:/Users/soon/Desktop/Soon_laser_cut_sorter", SmlCtorAttrTransfer.IgnoreAttr.IGNOREDTYPE | SmlCtorAttrTransfer.IgnoreAttr.IGNOREDNAME, True)
# laserSmlAttrTransfer.doRefactor()

from EnvironVariable import getNativePath
from SmlJsonTreeExplorerAttrTransfer import SmlJsonTreeExplorerAttrTransfer

dispensorTransfer = SmlJsonTreeExplorerAttrTransfer('C:/Users/soon/Desktop/Soon_dispenser_2021')
dispensorTransfer.doRefactor()

frameworkTransfer = SmlJsonTreeExplorerAttrTransfer(getNativePath() + "/..")
frameworkTransfer.doRefactor()

# skip
# laserTransfer = SmlJsonTreeExplorerAttrTransfer("C:/Users/soon/Desktop/Soon_laser_cut_sorter")
# laserTransfer.doRefactor()

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