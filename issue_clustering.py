#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: issue_clustering.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Mon Nov  2 15:33:33 2015
#########################################################################

import os
from kmedoids.kmedoids import kmedoids
from issue_routines import get_issue_list
from pprint import pprint

k = int(os.getenv("CLUSTER_K", 3))

def cluster_issues():
    issues = get_issue_list()
    print 'issues count:', len(issues)
    best_cost,best_choice,best_medoids = kmedoids(issues,k)
    issue_of_best_choice = []
    issue_of_best_medoids = []
    for choice in best_choice:
        issue_of_best_choice.append(issues[choice])
        issue_of_curr_choice = []
        for issue_i in best_medoids[choice]:
            issue_of_curr_choice.append(issues[issue_i])
        issue_of_best_medoids.append(issue_of_curr_choice)
    return best_cost,issue_of_best_choice,issue_of_best_medoids

if __name__ == '__main__' :
    best_cost,best_choice,best_medoids = cluster_issues()
    print 'best_cost:'
    pprint(best_cost)
    print 'best_choice:'
    pprint(best_choice)
    print 'best_medoids:'
    pprint(best_medoids)
