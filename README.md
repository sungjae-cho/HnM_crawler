# HnM_crawler
Make a web crawler mining the web page of H&amp;M US
* H&M US homepage to crawl: http://www.hm.com/us/

# Steps to do
1. Extract the image of an item page
   * Example: http://www.hm.com/us/product/72163?article=72163-A
2. Extract all the item links
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

# Data
* Items: 8528
  * Women: 6431
    * No sale: 5189
    * Sale: 1242
  * Men: 2097
    * No sale: 1490
    * Sale: 607
* All items have their images.
  * There are two kinds of images: item images, model images.
  * Items with one image: 1039 (Maybe they are all item images.)
  * Items with two images: 4568
* Image name: {W,M}{I,M}\_{serial numder}.jpg
  * {W, M}: 'W' means 'omen'. 'M' means 'Men'.
  * {I, M}: 'I means 'Item image'. 'M' means 'Model image'.
* Total image size: 251 MB

## Data maniplation
Make an interface that helps to import the information of items and images.
