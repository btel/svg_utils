from lxml import etree
from copy import deepcopy
import codecs

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

SVG_NAMESPACE = "http://www.w3.org/2000/svg"
XLINK_NAMESPACE = "http://www.w3.org/1999/xlink"
SVG = "{%s}" % SVG_NAMESPACE
XLINK = "{%s}" % XLINK_NAMESPACE
NSMAP = {None: SVG_NAMESPACE,
         'xlink': XLINK_NAMESPACE}


class FigureElement(object):
    """Base class representing single figure element"""
    def __init__(self, xml_element, defs=None):

        self.root = xml_element

    def moveto(self, x, y, scale=1):
        self.root.set("transform", "%s translate(%s, %s) scale(%s)" %
                      (self.root.get("transform") or '', x, y, scale))

    def rotate(self, angle, x=0, y=0):
        self.root.set("transform", "%s rotate(%f %f %f)" %
                      (self.root.get("transform") or '', angle, x, y))

    def __getitem__(self, i):
        return FigureElement(self.root.getchildren()[i])

    def copy(self):
        return deepcopy(self.root)

    def tostr(self):
        return etree.tostring(self.root, pretty_print=True)

    def find_id(self, element_id):
        find = etree.XPath("//*[@id=$id]")
        return FigureElement(find(self.root, id=element_id)[0])


class TextElement(FigureElement):
    """Text element.

    Corresponds to SVG ``<text>`` tag."""
    def __init__(self, x, y, text, size=8, font="Verdana",
                 weight="normal", letterspacing=0):
        txt = etree.Element(SVG+"text", {"x": str(x), "y": str(y),
                                         "font-size": str(size),
                                         "font-family": font,
                                         "font-weight": weight,
                                         "letter-spacing": str(letterspacing)})
        txt.text = text
        FigureElement.__init__(self, txt)


class ImageElement(FigureElement):
    """Inline image element.

    Correspoonds to SVG ``<image>`` tag. Image data encoded as base64 string.
    """
    def __init__(self, stream, width, height, format='png'):
        base64str = codecs.encode(stream.read(), 'base64').rstrip()
        uri = "data:image/{};base64,{}".format(format,
                                               base64str.decode('ascii'))
        attrs = {
                'width': str(width),
                'height': str(height),
                XLINK+'href': uri
                }
        img = etree.Element(SVG+"image", attrs)
        FigureElement.__init__(self, img)


class LineElement(FigureElement):
    """Line element.

    Corresponds to SVG ``<path>`` tag. It handles only piecewise
    straight segments
    """
    def __init__(self, points, width=1, color='black'):
        linedata = "M{} {} ".format(*points[0])
        linedata += " ".join(map(lambda x: "L{} {}".format(*x), points[1:]))
        line = etree.Element(SVG+"path",
                             {"d": linedata,
                              "stroke-width": str(width),
                              "stroke": color})
        FigureElement.__init__(self, line)


class GroupElement(FigureElement):
    """Group element.

    Container for other elements. Corresponds to SVG ``<g>`` tag.
    """
    def __init__(self, element_list, attrib=None):
        new_group = etree.Element(SVG+"g", attrib=attrib)
        for e in element_list:
            if isinstance(e, FigureElement):
                new_group.append(e.root)
            else:
                new_group.append(e)
        self.root = new_group


class SVGFigure(object):
    """SVG Figure.

    It setups standalone SVG tree. It corresponds to SVG ``<svg>`` tag.
    """
    def __init__(self, width=None, height=None):
        self.root = etree.Element(SVG+"svg", nsmap=NSMAP)
        self.root.set("version", "1.1")
        if width:
            self.width = width
        if height:
            self.height = height

    @property
    def width(self):
        """SVG width"""
        return self.root.get("width")

    @width.setter
    def width(self, value):
        self.root.set('width', str(value))
        self.root.set("viewbox", "0 0 %s %s" % (self.width, self.height))

    @property
    def height(self):
        """SVG height"""
        return self.root.get("height")

    @height.setter
    def height(self, value):
        self.root.set('height', str(value))
        self.root.set("viewbox", "0 0 %s %s" % (self.width, self.height))

    def append(self, element):
        try:
            self.root.append(element.root)
        except AttributeError:
            self.root.append(GroupElement(element).root)

    def getroot(self):
        if 'class' in self.root.attrib:
            attrib = {'class': self.root.attrib['class']}
        else:
            attrib = None
        return GroupElement(self.root.getchildren(), attrib=attrib)

    def to_str(self):
        """
        Returns a string of the svg image
        """
        return etree.tostring(self.root, xml_declaration=True,
                              standalone=True,
                              pretty_print=True)

    def save(self, fname):
        out = etree.tostring(self.root, xml_declaration=True,
                             standalone=True,
                             pretty_print=True)
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
    """Open SVG figure from file.

    Parameters
    ----------
    fname : str
        name of the SVG file

    Returns
    -------
    SVGFigure
        newly created :py:class:`SVGFigure` initialised with the file content
    """
    fig = SVGFigure()
    fid = open(fname)
    svg_file = etree.parse(fid)
    fid.close()

    fig.root = svg_file.getroot()
    return fig


def fromstring(text):
    """Create a SVG figure from a string.

    Parameters
    ----------
    text : str
        string representing the SVG content. Must be valid SVG.

    Returns
    -------
    SVGFigure
        newly created :py:class:`SVGFigure` initialised with the string
        content.
    """
    fig = SVGFigure()
    svg = etree.fromstring(text)

    fig.root = svg

    return fig


def from_mpl(fig):
    """Create a SVG figure from a ``matplotlib`` figure.

    Parameters
    ----------
    fig : matplotlib.Figure instance
        complete figure to be converted into SVG


    Returns
    -------
    SVGFigure
        newly created :py:class:`SVGFigure` initialised from the ``matplotlib``
        figure.
    """

    fid = StringIO()

    try:
        fig.savefig(fid, format='svg')
    except ValueError:
        raise(ValueError, "No matplotlib SVG backend")
    fid.seek(0)
    fig = fromstring(fid.read())

    # workaround mpl units bug
    w, h = fig.get_size()
    fig.set_size((w.replace('pt', ''), h.replace('pt', '')))

    return fig
