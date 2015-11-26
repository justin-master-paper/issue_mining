#!/usr/bin/python
#coding: utf8
#########################################################################
# File Name: calc_confidences.py
# Author: Justin Leo Ye
# Mail: justinleoye@gmail.com 
# Created Time: Thu Nov 26 23:42:28 2015
#########################################################################

from copy import deepcopy
from pprint import pprint

from db import db

rules = [
    (('serverity-cosmetic', 'type-user_interface'), 'priority-not_urgent', 22),
    (('root_cause-software'), 'origin-code', 34),
    (('root_cause-software', 'origin-code'), 'priority-normal_queue', 27),
    (('root_cause-software'), 'priority-normal_queue', 60),
    (('root_cause-software'), 'priority-normal_queue', 'serverity-cosmetic', 33),
    (('root_cause-people'), 'serverity-cosmetic', 'source-code', 23),
    (('type-build_package_merge'), 'priority-normal_queue', 22),
    (('root_cause-target'), 'source-requirement', 'priority-normal_queue', 28),
    (('source-requirement'), 'priority-normal_queue', 'serverity-cosmetic', 35),
    (('root_cause-software'), 'serverity-minor', 'priority-normal_queue', 26),
    (('root_cause-software', 'origin-code'), 'priority-normal_queue', 'serverity-minor', 31),
    (('root_cause-software'), 'source-code', 'origin-code', 20),
    (('root_cause-software'), 'source-code', 'serverity-cosmetic', 20),
    (('root_cause-software'), 'source-code', 'priority-normal_queue', 27),
    (('source-code'), 'origin-code', 34),
    (('root_cause-software'), 'priority-normal_queue', 'type-function', 56),
    (('root_cause-software'), 'source-code', 'type-function', 'priority-normal_queue', 28),
    ('type-function', 'source-code', 'origin-code', 'priority-normal_queue', 25),
    (('root_cause-people', 'source-requirement'), 'origin-requirement', 'serverity-cosmetic', 20)
]

def calc_all_confidences():
    confis = []
    for rule in rules:
        confi = calc_rule_confidence(rule)
        confis.append(confi)
    return confis


def calc_rule_confidence(rule):
    numerator_options, denominator_options = gen_find_options(rule)
    numerator = db_find(numerator_options) * 1.0
    denominator = db_find(denominator_options) * 1.0
    cunt = rule[-1] * 1.0

    return [denominator, cunt/denominator, numerator/denominator]


def gen_find_options(rule):
    denominator_options = {}
    for opt in rule[0]:
        key,value = opt.split('-')
        denominator_options[key] = value
    denominator_options['status'] = {'$ne': 'rejected'}
    numerator_options = deepcopy(denominator_options)
    for opt in rule[1:-1]:
        key,value = opt.split('-')
        numerator_options[key] = value
    return numerator_options, denominator_options

def db_find(options):
    return db.defects_classified.find(options).count()

if __name__ == '__main__':
    confidences = calc_all_confidences()
    pprint(confidences)
