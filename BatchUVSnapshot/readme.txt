
*** UV snapshot each selected object and save those files in given directory (defaults to desktop) with given file format (defaults to maya iff).***
** since maya 2017 is using pyside2 instead of pyside so this code might not be compatible with maya 2017! only works with maya 2016 or any maya version that uses pyside.

Install instruction:
    -save this script file in your maya script folder. (C:\Users\UserName\Documents\maya\2016\scripts\)

how to use in maya:
    -in the maya script editor, run the following python code to call the UI window:
        from BatchUVSnapshot import showUI
        ui = BatchUVUI.showUI()
    -select the object(s) that you wish to export the UV of.
    -by default, the UV will be saved on your desktop with the transform name, 1024 x 1024 in resolution, maya iff format.
