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
        routines.append([issue[key] for key in CLASSIFICATIONS_KEYS])
    return routines

def get_issue_routines():
    issues = get_all_classified_issues()
    return prepare_routines(issues)