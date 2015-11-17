#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: issue.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Sun Nov  1 13:37:02 2015
#########################################################################


from db import db

CLASSIFICATIONS_KEYS = ["type", "serverity", "priority", "status", "origin", "source", "root_cause"]

def get_all_classified_issues():
    issues = db.defects_classified.find()
    return issues

def prepare_routines(issues):
    routines = []
    for issue in issues:
        if issue["status"] == "rejected": continue
        routines.append([key+'-'+issue[key] for key in CLASSIFICATIONS_KEYS])
    return routines

def get_issue_routines():
    issues = get_all_classified_issues()
    return prepare_routines(issues)

def get_issue_list():
    issue_list = []
    issues = get_all_classified_issues()
    for issue in issues:
        issue_list.append(issue)
    return issue_list

