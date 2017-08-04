# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle

def import_items_info():
    pf = open('pickle_data/dict_items_info_with_tbo.p', 'rb')
    dict_items_info = pickle.load(pf)
    pf.close()
    return dict_items_info

def import_all_items_info():
    pf = open('pickle_data/dict_all_items_info.p', 'rb')
    dict_items_info = pickle.load(pf)
    pf.close()
    return dict_items_info

def import_tbo_categories():
    pf = open('pickle_data/dict_tbo_categories.p', 'rb')
    tbo_categories = pickle.load(pf)
    pf.close()
    return tbo_categories

def get_categories_from_serial(item_serial):
    dict_all_items_info = import_all_items_info()
    dict_tbo_categories = import_tbo_categories()
    categories = []
    for tbo in dict_tbo_categories.keys():
        for category in dict_tbo_categories[tbo]:
            metricCategoryID = dict_all_items_info[item_serial]['metricCategoryID']
            if metricCategoryID.find(category) != -1:
                categories.append(category)
    return categories