# HnM_crawler
Make a web crawler mining the web page of H&amp;M US
* H&M US homepage to crawl: http://www.hm.com/us/

## 1. Steps to extract the data
1. Extract all the item links
   * Items to extract: 
     * Women's, Men's
       * All women's items
         * No sale: http://www.hm.com/us/products/ladies
         * Sale: http://www.hm.com/us/products/sale/ladies
       * All men's items
         * No sale: http://www.hm.com/us/products/men
         * Sale: http://www.hm.com/us/products/sale/men
     * Categories to include: tops and bottoms that are not underwear
       * ['TOPS', 'BOTTOMS', 'SHIRT', 'VESTS' 'BLOUSES', 'DRESSES', 'JUMPSUITS', 'JEANS', 'PANTS', 'TROUSERS', 'CARDIGANS', 'SWEATERS', 'JUMPERS', 'HOODIES', 'SWEATSHIRTS', 'SHORTS', 'SKIRTS', 'JACKETS', 'COATS', 'BLAZERS', 'SUITS']
     * Categories to exclude: shoes, socks, accessories 
2. Extract the images and the other information from item pages
   * Example: http://www.hm.com/us/product/72163?article=72163-A
     * 72163: Design number
     * A: Color
     * 72163-A: Product serial number
3. Download the images of all the items 
4. Make an interface that helps to import the information of items and images.

## 2. Data
### 2.1. Data from the lists of all women's and men's items
* Items: 8528
  * Women: 6431
    * No sale: 5189
    * Sale: 1242
  * Men: 2097
    * No sale: 1490
    * Sale: 607

### 2.2. Data selected by some categories
* Items in the following categories: 5607
  * ['TOPS', 'BOTTOMS', 'SHIRT', 'VESTS' 'BLOUSES', 'DRESSES', 'JUMPSUITS', 'JEANS', 'PANTS', 'TROUSERS', 'CARDIGANS', 'SWEATERS', 'JUMPERS', 'HOODIES', 'SWEATSHIRTS', 'SHORTS', 'SKIRTS', 'JACKETS', 'COATS', 'BLAZERS', 'SUITS'] 

### 2.3. Data of extracted images
* All items have their images.
  * There are two kinds of images: __item images__, __model images__.
* Items to extract their images: __5607__
  * Items with zero images: 0
  * Items with one image: 1039 (Maybe they are all item images.)
  * Items with two images: __4568__
* Total images: __10175__
  * Images of the items with two images: __9136__
* Image name: {W,M}{I,M}\_{serial numder}.jpg
  * {W, M}: 'W' means 'Women'. 'M' means 'Men'.
  * {I, M}: 'I means 'Item image'. 'M' means 'Model image'.
* Total image size
  * 231 MB (logically)
  * 251 MB (on disk)

### 2.4. Data maniplation
I created a Python file able to help manipulate the downloaded images and item data.
* File name: interface.py
  * def import\_items\_info()
* How to use __interface__: Reference this [ipython noteobook 'guide\_to\_using\_interface.ipynb'](https://nbviewer.jupyter.org/github/phoenix2718/HnM_crawler/blob/master/5-10_guide_to_using_interface.ipynb)


### 2.5. Data containing the information of items
The following types of infromation are extracted.
* __serial__: The identification of an item
* __name__: The name of an item
* __who__: Sex in {'Women','Men'}
* __color__: In some item page, its color is not specified by any color name.
* __image__: Image URLs. Some have 1 image, the others have 2 images.
* __url__: The URL of the page for an item

