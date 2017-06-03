# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib
from HTMLParser import HTMLParser

class HnM_ProductPage_Parser(HTMLParser):
    in_head_tag = False
    in_title_tag = False
    image_found = False
    image_url = ""
    name = ""
    color = ""
    who = ""
    
    def handle_starttag(self, tag, attrs):
        if tag == "head":
            self.in_head_tag = True
        if tag == "title":
            self.in_title_tag = True
        if tag == "a":
            for attr in attrs:
                if attr[0] == "class" and attr[1] == "STILL_LIFE_FRONT":
                    self.image_found = True
            if self.image_found == True:
                for attr in attrs:
                    if attr[0] == "href":
                        self.image_url = attr[1]
                        self.image_found = False
        
    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head_tag = False
        if tag == "title":
            self.in_title_tag = False
            
    def handle_data(self, data):
        if self.in_head_tag and self.in_title_tag:
            if data[-1] == 'H':
                data_list = data.split(' | ')
                self.name =  data_list[0]
                self.color = data_list[1]
                self.who = data_list[2]
        
    def get_image_url(self):
        return "http:" + self.image_url
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_who(self):
        return self.who

item_url = "http://www.hm.com/us/product/72818?article=72818-A"
handle = urllib.urlopen(item_url)
html_gunk =  handle.read()
parser = HnM_ProductPage_Parser()
parser.feed(str(html_gunk))

item_serial = item_url[item_url.find("article=")+len("article="):]

print "Image URL: " + parser.get_image_url()
print "Name: " + parser.get_name()
print "Color: " + parser.get_color()
print "Who: " + parser.get_who()
print "Serial: " + item_serial

# url download
image_contents = urllib.urlopen(parser.get_image_url())

f = open(item_serial + ".jpg", "wb")
f.write(image_contents.read())
f.close()