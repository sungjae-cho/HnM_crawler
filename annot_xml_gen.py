from lxml import etree
import os

def del_extension(string):
    return string[:string.rfind('.')]

def annotdict_to_annotxml(d, dir_xml):
    '''
    d: dictionary
    dir_xml: directory to store annotation XML files
    '''
    # 0. Annotate to the annotation tag
    
    root_tag = etree.Element('annotation')

    folder_tag = etree.Element('folder')
    folder_tag.text =  d['folder']
    root_tag.append(folder_tag)

    filename_tag = etree.Element('filename')
    filename_tag.text = d['filename']
    root_tag.append(filename_tag)

    source_tag = etree.Element('source')
    root_tag.append(source_tag)

    owner_tag = etree.Element('owner')
    root_tag.append(owner_tag)

    size_tag = etree.Element('size')
    root_tag.append(size_tag)

    segmented_tag = etree.Element('segmented')
    root_tag.append(segmented_tag)

    object_tag = etree.Element('object')
    root_tag.append(object_tag)
    
    # 1. Annotate to the source tag
    
    database_tag = etree.Element('database')
    source_tag.append(database_tag)

    annotation_tag = etree.Element('annotation')
    source_tag.append(annotation_tag)

    image_tag = etree.Element('image')
    source_tag.append(image_tag)

    flickrid_tag = etree.Element('flickrid')
    source_tag.append(flickrid_tag)
    
    # 2. Annotate to the owner tag
    
    flickrid_tag = etree.Element('flickrid')
    owner_tag.append(flickrid_tag)

    name_tag = etree.Element('name')
    owner_tag.append(name_tag)
    
    # 3. Annotate to the size tag
    
    width_tag = etree.Element('width')
    width_tag.text = d['size']['width']
    size_tag.append(width_tag)

    height_tag = etree.Element('height')
    height_tag.text = d['size']['height']
    size_tag.append(height_tag)

    depth_tag = etree.Element('depth')
    size_tag.append(depth_tag)
    
    # 4. Annotate to the object tag
    
    name_tag = etree.Element('name')
    name_tag.text = d['object']['name']
    object_tag.append(name_tag)

    pose_tag = etree.Element('pose')
    object_tag.append(pose_tag)

    truncated_tag = etree.Element('truncated')
    object_tag.append(truncated_tag)

    difficult_tag = etree.Element('difficult')
    object_tag.append(difficult_tag)

    bndbox_tag = etree.Element('bndbox')
    object_tag.append(bndbox_tag)

    xmin_tag = etree.Element('xmin')
    xmin_tag.text = d['object']['bndbox']['xmin']
    bndbox_tag.append(xmin_tag)

    ymin_tag = etree.Element('ymin')
    ymin_tag.text = d['object']['bndbox']['ymin']
    bndbox_tag.append(ymin_tag)

    xmax_tag = etree.Element('xmax')
    xmax_tag.text = d['object']['bndbox']['xmax']
    bndbox_tag.append(xmax_tag)

    ymax_tag = etree.Element('ymax')
    ymax_tag.text = d['object']['bndbox']['ymax']
    bndbox_tag.append(ymax_tag)
    
    directory = 'images_items_annotation'
    if not os.path.exists(dir_xml):
        os.makedirs(dir_xml)
    f = open(dir_xml + '/' + del_extension(d['filename']) + '.xml', 'wb')
    s = etree.tostring(root_tag, pretty_print=True)
    f.write(s)
    f.close()