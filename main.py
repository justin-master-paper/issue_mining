#coding=utf-8
from fp_growth import tree_builder, tree_miner
from issue_routines import get_issue_routines

routines = get_issue_routines()
min_sup = int(len(routines) * 0.1)                             #最小支持度计数
headerTable = {}        #头结点表，用来存放各个项的索引

treeBuilder = tree_builder.Tree_builder(routines=routines, min_sup=min_sup, headerTable=headerTable)    #建造FP_Tree
tree_miner.Tree_miner(Tree=treeBuilder.tree, min_sup=min_sup, headerTable=headerTable)         #对FP_Tree进行频繁项集的挖掘
