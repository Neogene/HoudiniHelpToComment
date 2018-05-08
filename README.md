# HoudiniHelpToComment
A script which auto populate NEW nodes comment with online documentation headline

## AUTHOR: ## 
eng. ANDREA LEGANZA

## TESTED VERSION/S: ## 
HOUDINI 16/16.5

## DESCRIPTION: ## 
When learning Houdini it may be hard to undestand the flow of nodes and to take a sneak peak on the purpose of a single node: a user has to select right click on node -> help and wait for Houdini internal browser to load the help page. This script simply read node headline (the title) from the internal documentation ad uses to populate the node comment.

## INSTALLATION: ##
1. place script inside  <$houdini>/scripts/ 
2. restart Houdini
3. create a geometry node
4. inside it create any kind of node
5. script will add for any new node as comment the headline taken from online documentation

## NOTE: ## 
Some nodes don't have headline or the whole documentation file.

## CONTRIBUTING: ##
Please feel free to optimize the script and add/report missing nodes documentation. 