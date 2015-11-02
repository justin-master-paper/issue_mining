#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: issue_clustering.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Mon Nov  2 15:33:33 2015
#########################################################################

from kmedoids.kmedoids import kmedoids
from issue_routines import get_issue_list
from pprint import pprint

k = 3

def cluster_issues():
    issues = get_issue_list()
    print 'issues:'
    pprint(issues)
    return kmedoids(issues,k)

if __name__ == '__main__' :
    best_cost,best_choice,best_medoids = cluster_issues()
    pprint(best_cost)
    pprint(best_choice)
    pprint(best_medoids)
