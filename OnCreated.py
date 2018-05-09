#!/usr/bin/python
#TILE: HOUDINI HELP TO COMMENT
#AUTHOR: eng. ANDREA LEGANZA
#HOUDINI VERSION: TESTED ON HOUDINI 16.0 AND 16.5
#SCRIPT VERSION: 1.0
#DESCRIPTION:
# 1) place script inside  <$houdini>/scripts/ 
# 2) restart Houdini
# 3) create a geometry node
# 4) inside it create any kind of node
# 5) script will add for any new node as comment the headline taken from online documentation
# NOTE: some scripts don't have headline or entire documentation 

import hou
import os
import zipfile

ZIPFOLDER = os.environ['HFS']+"/houdini/help/nodes.zip".replace("/",os.sep)
ARCHIVE = zipfile.ZipFile(ZIPFOLDER, 'r')
   
def getHeader(path):
    path = path.replace("operator:","").split("?")[0]
    path = path.lower()
    nodeHelpContent = ARCHIVE.read(path+".txt")
    splitted = nodeHelpContent.split("\"\"\"")
    return splitted[1] if len(splitted)>1 else "Not found"

def main(kwargs):

    node = kwargs["node"]

    if len(node.comment())==0 :
        description = getHeader(node.type().defaultHelpUrl())
        node.setComment(description)
        node.setGenericFlag(hou.nodeFlag.DisplayComment,True)
    

main(kwargs)