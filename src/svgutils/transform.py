from lxml import etree
from copy import deepcopy
import re
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

SVG_NAMESPACE = "http://www.w3.org/2000/svg"
SVG = "{%s}" % SVG_NAMESPACE
NSMAP = {None : SVG_NAMESPACE}

class FigureElement(object):

    def __init__(self, xml_element, defs=None):
        
        self.root = xml_element 

    def moveto(self, x, y, scale=1):
        self.root.set("transform", "%s translate(%s, %s) scale(%s)" %
                (self.root.get("transform") or '', x,y, scale))

    def rotate(self, angle, x=0, y=0):
        self.root.set("transform", "%s rotate(%f %f %f)" %
                (self.root.get("transform") or '', angle,x, y))


    def __getitem__(self, i):
        return FigureElement(self.root.getchildren()[i])

    def copy(self):
        return deepcopy(self.root)


class TextElement(FigureElement):
    def __init__(self, x, y, text, size=8, font="Verdana",
            weight="normal"):
        txt = etree.Element(SVG+"text", {"x": str(x), "y": str(y),
            "font-size":str(size), "font-family": font,
            "font-weight": weight})
        txt.text = text
        FigureElement.__init__(self, txt)

class GroupElement(FigureElement):
    def __init__(self, element_list):
        new_group = etree.Element(SVG+"g")
        for e in element_list:
            if isinstance(e, FigureElement):
                new_group.append(e.root)
            else:
                new_group.append(e)
        self.root = new_group


class SVGFigure(object):
    def __init__(self, width=None, height=None):
        self.root = etree.Element(SVG+"svg",nsmap=NSMAP)
        self.root.set("version", "1.1")
        if width or height:
            self.root.set("width", width)
            self.root.set("height",  height)
            self.root.set("viewbox", "0 0 %s %s" % (width, height))
    def append(self,element):
        try:
            self.root.append(element.root)
        except AttributeError:
            self.root.append(GroupElement(element).root)

    def getroot(self):
        return GroupElement(self.root.getchildren())
        
    def to_str(self):
        """
        Returns a string of the svg image 
        """
        return etree.tostring(self.root, xml_declaration=True, 
                standalone=True,pretty_print=True)    
 

    def save(self, fname):
        out=etree.tostring(self.root, xml_declaration=True, 
                standalone=True,pretty_print=True)
        fid = open(fname, 'wb')
        fid.write(out)
        fid.close()
    
    def find_id(self, element_id):
        find = etree.XPath("//*[@id=$id]")
        return FigureElement(find(self.root, id=element_id)[0])

    def get_size(self):
        return self.root.get('width'), self.root.get('height')
    
    def set_size(self, size):
        w, h = size
        self.root.set('width', w)
        self.root.set('height', h)

def fromfile(fname):
    fig = SVGFigure()
    fid = open(fname)
    svg_file = etree.parse(fid)
    fid.close()

    fig.root = svg_file.getroot() 
    return fig

def fromstring(text):
    fig = SVGFigure()
    svg = etree.fromstring(text)

    fig.root = svg

    return fig

def from_mpl(fig):

    fid = StringIO()

    try:
        fig.savefig(fid, format='svg')
    except ValueError:
        raise(ValueError, "No matplotlib SVG backend")
    fid.seek(0)
    fig =  fromstring(fid.read())

    #workaround mpl units bug
    w,h = fig.get_size()
    fig.set_size((w.replace('pt', ''), h.replace('pt', '')))

    return fig
