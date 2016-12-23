"""
Harden the UV border edges of selected objects (similar to assigning different smooth groups in 3DSMax)
it's a necessary preparation for normal map baking in some workflows.

Instruction:
    -select the obj(S) that you wish to harden the uv border for
    -copy & paste this python code in Maya script editor and run it!
    -check the result and smooth any unwanted hard edges. This usually happens at the UV seam that runs across 
     a smooth surface.
"""

from maya import cmds


# get a list of selected objs
currentSelectedObjs = cmds.ls(sl=True)

# select each obj in that list and get its total number of edges
for obj in range(len(currentSelectedObjs)):
    currentSelectedObj = currentSelectedObjs[obj]
    cmds.select(str(currentSelectedObj))
    totalNumberOfEdge = cmds.polyEvaluate(edge=True)

    # iterate through each edge and find the UV border edges (the edge that contains more than 2 UV points) 
    # of each selected obj
    borderEdges = []
    for i in range(totalNumberOfEdge):
        currentEdge = '%s.e[%s]' % (currentSelectedObj, i)
        currentUVPoints = cmds.polyListComponentConversion(currentEdge, tuv=True)
        numberOfUVPoints = len(cmds.ls(currentUVPoints, flatten=True))
        if (numberOfUVPoints > 2):
            borderEdges.append(currentEdge)
    print borderEdges
    # finally, harden the border edge!
    cmds.select(borderEdges, r=True)
    cmds.polySoftEdge(angle=0, caching=True)
