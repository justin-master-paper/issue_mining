#coding=utf-8
from fp_growth import tree_builder, tree_miner
from issue_routines import get_issue_routines
from consts import DEFECT_CLAS_LIST, DEFECT_CLASSIFICATIONS 

routines = get_issue_routines()
min_sup = int(len(routines) * 0.1)                             #最小支持度计数
print '#'*40
print 'min_sup:', min_sup
print '#'*40
headerTable = {}        #头结点表，用来存放各个项的索引

def showResult(result=[[]]):
    """功能: 将挖掘到的频繁项集进行展示"""
    for elem in result:
        rule = []
        cnt = 0
        for item in elem:
            if (type(item) == str or type(item) ==unicode) and item not in rule:
                rule.append(item)
            if type(item) == int:
                cnt = item
        rule.append(cnt)
        print tuple(rule)
    return

treeBuilder = tree_builder.Tree_builder(routines=routines, min_sup=min_sup, headerTable=headerTable)    #建造FP_Tree
tree_miner.Tree_miner(Tree=treeBuilder.tree, min_sup=min_sup, headerTable=headerTable, showResult=showResult)         #对FP_Tree进行频繁项集的挖掘

