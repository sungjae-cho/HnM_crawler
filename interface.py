# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle

def import_items_info():
    pf = open('pickle_data/dict_items_info.p', 'rb')
    dict_items_info = pickle.load(pf)
    pf.close()
    return dict_items_info

def import_tbo_categories():
    pf = open('pickle_data/dict_tbo_categories.p', 'rb')
    tbo_categories = pickle.load(pf)
    pf.close()
    return tbo_categories