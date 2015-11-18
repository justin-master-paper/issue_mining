#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: issue_correlation_on_time.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Tue Nov  3 12:56:59 2015
#########################################################################

import os
from pprint import pprint
from issue_clustering import cluster_issues
from fp_growth import tree_builder, tree_miner
from issue_routines import get_issue_routines

window_size = int(os.getenv('WINDOW_SIZE', 3))
print '*'*40
print 'window_size:',window_size
print '*'*40

def issue_cluster_distribute_by_repo(medoids):
    issues_by_repo = {}
    cnt = len(medoids)
    for i in range(cnt):
        cluster = medoids[i]
        while len(medoids[i]) > 0:
            issue = medoids[i].pop()
            issue['cluster'] = 'c'+str(i)
            try:
                issues_by_repo[issue['repo']].append(issue)
            except KeyError,e:
                print 'error:',e
                issues_by_repo[issue['repo']] = [issue]
    #print '*'*40
    #print 'issues_by_repo:'
    #pprint(issues_by_repo)
    return issues_by_repo

def sort_issues_by_repo(issues_by_repo):
    #print 'issues_by_repo:'
    #pprint(issues_by_repo)
    for key,issue_list in issues_by_repo.iteritems():
        issue_list.sort(key=lambda x: x['number'])
    return issues_by_repo

def do_issue_cluster_distribute_by_repo():
    best_cost, best_choice, best_medoids = cluster_issues()
    issues_by_repo = issue_cluster_distribute_by_repo(best_medoids)
    issues_by_repo_sorted = sort_issues_by_repo(issues_by_repo)
    #print '*'*40
    #pprint(issues_by_repo_sorted)

    return issues_by_repo_sorted

def generate_issue_routines(issues_sorted):
    routines = []
    window = []
    for issue in issues_sorted:
        if len(window) == window_size:
            routines.append(list(set(window)))
            del window[0]
        window.append(issue['cluster'])
    return routines

def issue_mining_on_timescale():
    issues_by_repo_sorted = do_issue_cluster_distribute_by_repo()
    for repo,issues_sorted in issues_by_repo_sorted.iteritems():
        #print 'issues_sorted:'
        #pprint(issues_sorted)
        routines = generate_issue_routines(issues_sorted)
        print '+'*40
        pprint(routines)
        print '+'*40

        min_sup_percent = float(os.getenv('CLUSTER_MIN_SUP_PERCENT', 0.1))
        min_sup = int(len(routines) * min_sup_percent)                             #最小支持度计数

        print '#'*40
        print 'min_sup:', min_sup
        print 'len of current routines:',len(routines)
        print '#'*40
        if min_sup <= 0:
            print 'current routines is too short'
            continue

        headerTable = {}        #头结点表，用来存放各个项的索引

        treeBuilder = tree_builder.Tree_builder(routines=routines, min_sup=min_sup, headerTable=headerTable)    #建造FP_Tree
        tree_miner.Tree_miner(Tree=treeBuilder.tree, min_sup=min_sup, headerTable=headerTable, showResult=showResult)         #对FP_Tree进行频繁项集的挖掘

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


if __name__ == '__main__':
    issue_mining_on_timescale()
