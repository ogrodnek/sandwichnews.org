from __future__ import absolute_import
from __future__ import unicode_literals
from urlparse import urljoin

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree

class ImageCaptionExtension(Extension):
    def __init__(self, configs=[]):
      pass

    def extendMarkdown(self, md, md_globals):
        image_caption = ImageCaptionTreeprocessor(md)
        image_caption.config = self.getConfigs()
        md.treeprocessors.add("imagecaption", image_caption, "_end")
        md.registerExtension(self)


class ImageCaptionTreeprocessor(Treeprocessor):
    def run(self, root):
        for i, p in enumerate(root.getchildren()):
          if p.tag == 'img' and 'alt' in p.attrib:
            elem = root.makeelement('figure', {})
            root[i] = elem
            elem.append(p)
            caption = etree.SubElement(elem, 'figcaption')
            caption.text = p.attrib['alt']
          self.run(p)

def makeExtension(configs=[]):
    return ImageCaptionExtension(configs=configs)
