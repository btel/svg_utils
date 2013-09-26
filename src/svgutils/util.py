import copy
import re

def svg_id_prepend(root, prefix):
    """Append prefix to id attributes and url(#id) references"""

    root = copy.deepcopy(root)

    id_attributes = {}
    ## Replace id attributes
    for e in root.findall("*//*[@id]"):
        idvalue = e.attrib['id']
        newidvalue = prefix + idvalue
        e.attrib['id'] = newidvalue
        
        id_attributes[idvalue] = newidvalue
        
    ## Update references
    for e in root.xpath("//*[contains(@*, 'url(#')]"):
        for attr, value in e.attrib.items():
            matchobj = re.match('url\(#(.*)\)', value)
            if matchobj and matchobj.groups()[0] in id_attributes:
                e.attrib[attr] = 'url(#%s)' % id_attributes[matchobj.groups()[0]]

    return root
