# HnM_crawler
Make a web crawler mining clothing images from the web pages of H&amp;M US.
* H&M US homepage to crawl: http://www.hm.com/us/
* For each item page, extract a worn image and a full single item image.

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
       * The following categories are gathered from the categories in the H&M Webpages.
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
* How to use __interface__: Reference this [ipython notebook '4-10\_guide\_to\_using\_interface.ipynb'](https://nbviewer.jupyter.org/github/phoenix2718/HnM_crawler/blob/master/4-10_guide_to_using_interface.ipynb)


### 2.5. Data containing the information of items
The following types of infromation are extracted.
* __serial__: The identification of an item
* __name__: The name of an item
* __who__: Sex in {'Women','Men'}
* __color__: The color of an item. In some item page, its color is not specified by any color name.
* __image__: Image URLs. Some have 1 image, the others have 2 images.
* __url__: The URL of the page for an item

## 3. Analyzing the categoreis
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
* Image name
  * {item\_serial}\_{I,M}{W,M}{T,B,O}.jpg
    * {item\_serial}: ID of an item
    * {I,M}: Item, or Model
    * {W,M}: Women, or Men
    * {T,B,O}: Top, Botttom, or Onepiece
