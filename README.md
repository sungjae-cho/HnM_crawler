# HnM_crawler
Make a web crawler mining clothing images from the web pages of H&amp;M US.
* H&M US homepage to crawl: http://www.hm.com/us/
* For each item page, extract a worn image and a full single item image.

## 1. Steps to proceed this project
1. Extract all the item links
   * Items to extract: 
     * Women's, Men's
       * All women's items
         * No sale: http://www.hm.com/us/products/ladies
         * Sale: http://www.hm.com/us/products/sale/ladies
       * All men's items
         * No sale: http://www.hm.com/us/products/men
         * Sale: http://www.hm.com/us/products/sale/men
2. Extract the images and the other information from all item pages.
   * Example: http://www.hm.com/us/product/72163?article=72163-A
     * 72163: Design number
     * A: Color
     * 72163-A: Product serial number
3. Investigate which categories to download. 
4. Download the images of all the items that has the candidate categories. 
5. Make an interface that helps to import the information of items and images.
6. Split all the images into two sets: images of items and images of models.
7. Extract the width and height of item images. Then, form XML files to contain the data.

## 2. Data
### 2.1. Item information from the lists of all women's and men's items
* Items: 8528
  * Women: 6431
    * No sale: 5189
    * Sale: 1242
  * Men: 2097
    * No sale: 1490
    * Sale: 607

### 2.2. Data containing the information of items
The following types of infromation are extracted.
* item\_info['serial']: The identification of an item
* item\_info['name']: The name of an item
* item\_info['who']: Sex in {'Women','Men'}
* item\_info['color']: The color of an item. In some item page, its color is not specified by any color name.
* item\_info['image']['item']: Image URL of an item without a model 
* item\_info['image']['model']: Image URL of a model wearing the item
* item\_info['url']: The URL of the page for an item
* item\_info['metricCategoryID']: the string chunk of categories of an item
* item\_info['tbo']: Top, bottom, or onepiece

### 2.3. Example: item\_info
```
>>> print item_info
{'color': 'Dark denim blue rugged rinse',
 'image': {
   'item': 'http://lp.hm.com/hmprod?set=key[source],value[/model/2016/D00 0399136 004 97 4998.jpg]&set=key[rotate],value[]&set=key[width],value[]&set=key[height],value[]&set=key[x],value[]&set=key[y],value[]&set=key[type],value[STILL_LIFE_FRONT]&set=key[hmver],value[1]&call=url[file:/product/large]',
   'model': 'http://lp.hm.com/hmprod?set=key[source],value[/environment/2016/8AQ_0096_013R.jpg]&set=key[rotate],value[0]&set=key[width],value[4306]&set=key[height],value[5034]&set=key[x],value[485]&set=key[y],value[87]&set=key[type],value[FASHION_FRONT]&set=key[hmver],value[0]&call=url[file:/product/large]'
   },
 'metricCategoryID': 'LADIES_JEANS_SHAPING_W198',
 'name': 'Shaping Skinny Regular Jeans',
 'serial': '47463-D',
 'tbo': 'bottom',
 'url': 'http://www.hm.com/us/product/47463?article=47463-D',
 'who': 'Women'
 }
 ```

## 3. Analyzing the categoreis and investigate which categories to download
* Superset categories
  * ['ACC', 'SPORTSWEAR', 'LONG', 'TUNICS', 'LINGERIE', 'JACKETS', 'MODERN-CLASSICS', 'SHORT', 'TOPS', 'BATH', 'SOCKS', 'HM', 'BATHROOM', 'PQ', 'VESTS', 'MODERNCLASSICS', 'JEANS', 'BOTTOMS', 'SKIRTS', 'SUITS', 'HAIR', 'LEGGINGS', 'ACCESSORIES', 'NIGHTWEAR', 'SHORTS', 'DIVIDED', 'SLIM', 'BASICS', 'SWIMWEAR', 'BLAZERS', 'TSHIRT', 'SHIRTS', 'CASUAL', 'JUMPSUIT', 'TIGHTS', 'UNDERWEAR', 'BEAUTY', 'DRESSED', 'TROUSERS', 'DRESSES', 'SLEEVED', 'HOODIES', 'SHOES', 'MIDI', 'LOOSE', 'PARTYWEAR']
* Categories to include
  * tops, bottoms, one-piece, non-underwear
  * tops
    * ['JACKETS', 'TOPS', 'VESTS', 'BLAZERS', 'TSHIRT', 'SHIRTS', 'HOODIES']
  * bottoms
    * ['JEANS', 'BOTTOMS', 'SKIRTS', 'LEGGINGS', 'SHORTS', 'TROUSERS']
  * onepiece
    * ['TUNICS', 'JUMPSUIT', 'DRESSES']
  * I will call the three categories the __TBO categories__: Tops, Bottoms, and Onepieces.
* The number of items that has a particular number of TBO categories (5-11\_category\_analysis\_for\_all\_items.ipynb)
  * 0 TBO categories: 3326 (ignore) (These are like accesories, shoes, hats, etc..)
  * 1 TBO category: 5108 (to deal with)
  * 2 TBO categories: 94 (ignore)
  * 3 TBO categories: 0
* The number of items in the TBO categories: 5108 (Women: 3712, Men: 1396)
  * The number of tops: 2811 (Women: 1886, Men: 925)
  * The number of bottoms: 1474 (Women: 1003, Men: 471)
  * The number of onepieces: 823 (Women: 823, Men: 0)


## 4. Images
* All the images are downloaded in the folder 'images\_clothes'.

### 4.1. Image name
* {item\_serial}\_{I,M}{W,M}{T,B,O}.jpg
  * {item\_serial}: ID of an item
  * {I,M}: Item, or Model
  * {W,M}: Women, or Men
  * {T,B,O}: Top, Botttom, or Onepiece

### 4.2. Image Count
* Total images: 5108
  * Items with 0 image: 0
    * Women    (0 image): 0
    * Men      (0 image): 0
    * Top      (0 image): 0
    * Bottom   (0 image): 0
    * Onepiece (0 image): 0
  * Items with 1 image: 981
    * Women    (1 image): 637
    * Men      (1 image): 344
    * Top      (1 image): 526
    * Bottom   (1 image): 235
    * Onepiece (1 image): 220
  * Items with 2 images: 4127
    * Women    (2 images): 3075
    * Men      (2 images): 1052
    * Top      (2 images): 2285
    * Bottom   (2 images): 1239 
    * Onepiece (2 images): 603
* __Error__
  * The number of images: 9185 (But we had 9235(=981+2\*4127) image URLs.)
* Capacity
  * Logical size: 209 MB
  * Physical size: 227 MB

### 4.3. Image folders
* 'images\_clothes': the images of all items
* 'images\_items': the images with only item without a model 
* 'images\_models': the images with a model 

## 5. Data maniplation
I created a Python file able to help manipulate the downloaded images and item data.
* File name: interface.py
  * def import\_items\_info()
* How to use __interface__: Reference this [ipython notebook '4-10\_guide\_to\_using\_interface.ipynb'](https://nbviewer.jupyter.org/github/phoenix2718/HnM_crawler/blob/master/4-10_guide_to_using_interface.ipynb)
* Reference Section 2.2..

## 6. Split image into two sets: images\_items and images\_models
* 'images\_items': the images with only item without a model 
* 'images\_models': the images with a model 
