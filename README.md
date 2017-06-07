# HnM_crawler
Make a web crawler mining the web page of H&amp;M US
* H&M US homepage to crawl: http://www.hm.com/us/

# Steps to do
1. Extract all the item links
   * Items to extract: 
     * women's, men's
     * Include: tops and bottoms that are not underwear
       * ['TOPS', 'BOTTOMS', 'SHIRT', 'VESTS' 'BLOUSES', 'DRESSES', 'JUMPSUITS', 'JEANS', 'PANTS', 'TROUSERS', 'CARDIGANS', 'SWEATERS', 'JUMPERS', 'HOODIES', 'SWEATSHIRTS', 'SHORTS', 'SKIRTS', 'JACKETS', 'COATS', 'BLAZERS', 'SUITS']
     * Exclude: shoes, socks, accessories 
   * All women's items
     * No sale: http://www.hm.com/us/products/ladies
     * Sale: http://www.hm.com/us/products/sale/ladies
   * All men's items
     * No sale: http://www.hm.com/us/products/men
     * Sale: http://www.hm.com/us/products/sale/men
2. Extract the image of an item page
   * Example: http://www.hm.com/us/product/72163?article=72163-A
3. Make an interface that helps to import the information of items and images.

# Data
## Data from the lists of all women's and men's items
* Items: 8528
  * Women: 6431
    * No sale: 5189
    * Sale: 1242
  * Men: 2097
    * No sale: 1490
    * Sale: 607

## Data containing the information of items
The following types of infromation are extracted.
* __serial__: The identification of each item
* __name__
* __who__: Sex in {'Women','Men'}
* __color__: In some item page, its color is not specified by any color name.
* __image__: Image URLs. Some have 1 image, the others have 2 images each.
* __url__: The URL of each item page

## Data excluding accessories
* Items in the following categories: 5607
  * ['TOPS', 'BOTTOMS', 'SHIRT', 'VESTS' 'BLOUSES', 'DRESSES', 'JUMPSUITS', 'JEANS', 'PANTS', 'TROUSERS', 'CARDIGANS', 'SWEATERS', 'JUMPERS', 'HOODIES', 'SWEATSHIRTS', 'SHORTS', 'SKIRTS', 'JACKETS', 'COATS', 'BLAZERS', 'SUITS'] 

## Data of extracted images
* All items have their images.
  * There are two kinds of images: item images, model images.
* Items to extract their images: 5607
  * Items with zero images: 0
  * Items with one image: 1039 (Maybe they are all item images.)
  * Items with two images: 4568
* Image name: {W,M}{I,M}\_{serial numder}.jpg
  * {W, M}: 'W' means 'Women'. 'M' means 'Men'.
  * {I, M}: 'I means 'Item image'. 'M' means 'Model image'.
* Total image size
  * 231 MB (logically)
  * 251 MB (on disk)


## Data maniplation
* File name: interface.py
  * def import\_items\_info()
* How to use __interface__: reference this [ipython noteobook 'guide\_to\_using\_interface.ipynb'](https://nbviewer.jupyter.org/github/phoenix2718/HnM_crawler/blob/master/5-10_guide_to_using_interface.ipynb)
