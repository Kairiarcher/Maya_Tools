"""
Harden the UV border edges of selected objects (similar to assigning different smooth groups in 3DSMax)
it's a necessary preparation for normal map baking in some workflows.

Instruction:
    -select the obj(S) that you wish to harden the uv border for
    -copy & paste this python code in Maya script editor and run it!
    -check the result and smooth any unwanted hard edges. This usually happens at the UV seam that runs across 
     a smooth surface.
"""