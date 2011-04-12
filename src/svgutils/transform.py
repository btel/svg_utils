from lxml import etree
from copy import deepcopy

SVG_NAMESPACE = "http://www.w3.org/2000/svg"
SVG = "{%s}" % SVG_NAMESPACE
NSMAP = {None : SVG_NAMESPACE}

class FigureElement(object):

    def __init__(self, xml_element, defs=None):
        
        self.root = xml_element 

    def moveto(self, x, y, scale=1):
        self.root.set("transform", "translate(%f, %f) scale(%f)" %
                (x,y, scale))

    def rotate(self, angle, x=0, y=0):
        self.root.set("transform", "rotate(%f %f %f)" %
                (angle,x, y))


    def __getitem__(self, i):
        return FigureElement(self.root.getchildren()[i])

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

#class MetaDataElement(FigureElement):
#    def __init_(self):
#        self.root = etree.Element(SVG+"metadata")
#    def __
        

class SVGFigure(object):
    def __init__(self, width=None, height=None):
        if width or height:
            self.root = etree.Element(SVG+"svg",nsmap=NSMAP)
            self.root.set("width", width)
            self.root.set("height",  height)
            self.root.set("version", "1.1")
    def append(self,element):
        try:
            self.root.append(element.root)
        except AttributeError:
            self.root.append(GroupElement(element).root)

    def getroot(self):
        return GroupElement(self.root.getchildren())
    def save(self, fname):
        out=etree.tostring(self.root, xml_declaration=True, 
                standalone=True,pretty_print=True)
        fid = file(fname, 'w')
        fid.write(out)
        fid.close()
    
    def find_id(self, element_id):
        find = etree.XPath("//*[@id=$id]")
        return FigureElement(find(self.root, id=element_id)[0])

def fromfile(fname):
    fig = SVGFigure()
    fid = open(fname)
    svg_file = etree.parse(fid)
    fid.close()

    fig.root = svg_file.getroot() 
    return fig


if __name__ == '__main__':
    
    fig = fromfile("../figRecruitCurve.svg")
    plot = fig.getroot()[0]
    plot.moveto(100, 100)
    fig.save("transformed2.svg")

    #new_figure = SVGFigure("2cm", "8cm")
    #new_figure.add_element(plot)
    #new_figure.save("transformed2.svg")


#ellipse =  etree.Element(SVG+"ellipse", {"cx":"2cm", "cy":"4cm",
#    "rx":"2cm", "ry":"1cm"},nsmap=NSMAP)



