#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: kmedoids.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Sun Nov  1 16:35:26 2015
#########################################################################

import random

CLASSIFICATIONS_KEYS = ["type", "serverity", "priority", "status", "origin", "source", "root_cause"]
max_issue_distance = len(CLASSIFICATIONS_KEYS)+1
distances_cache = {}

def issue_distance(item1, item2):
    dis = 0
    for key in CLASSIFICATIONS_KEYS:
        if item1[key] != item2[key]:
            dis += 1
    return dis

def totalcost(classified_issues, costf, medoids_idx) :
    size = len(classified_issues)
    total_cost = 0.0
    medoids = {}
    for idx in medoids_idx :
        medoids[idx] = []
    for i in range(size) :
        choice = None
        min_cost = max_issue_distance
        for m in medoids :
            tmp = distances_cache.get((m,i),None)
            if tmp == None :
                tmp = issue_distance(classified_issues[m],classified_issues[i])
                distances_cache[(m,i)] = tmp
            if tmp < min_cost :
                choice = m
                min_cost = tmp
        medoids[choice].append(i)
        total_cost += min_cost
    return total_cost, medoids
    

def kmedoids(classified_issues, k) :
    size = len(classified_issues)
    medoids_idx = random.sample([i for i in range(size)], k)
    pre_cost, medoids = totalcost(classified_issues,issue_distance,medoids_idx)
    print pre_cost
    current_cost = max_issue_distance * size # maxmum of pearson_distances is 2.    
    best_choice = []
    best_res = {}
    iter_count = 0
    while 1 :
        for m in medoids :
            for item in medoids[m] :
                if item != m :
                    idx = medoids_idx.index(m)
                    swap_temp = medoids_idx[idx]
                    medoids_idx[idx] = item
                    tmp,medoids_ = totalcost(classified_issues,issue_distance,medoids_idx)
                    #print tmp,'-------->',medoids_.keys()
                    if tmp < current_cost :
                        best_choice = list(medoids_idx)
                        best_res = dict(medoids_)
                        current_cost = tmp
                    medoids_idx[idx] = swap_temp
        iter_count += 1
        print current_cost,iter_count
        if best_choice == medoids_idx : break
        if current_cost <= pre_cost :
            pre_cost = current_cost
            medoids = best_res
            medoids_idx = best_choice

    return current_cost, best_choice, best_res
