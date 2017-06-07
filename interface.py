# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle

def import_items_info():
    pf = open('dict_items_info.p', 'rb')
    dict_items_info = pickle.load(pf)
    pf.close()
    return dict_items_info
