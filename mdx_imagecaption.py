from typing import Any
from xml.etree import ElementTree

from markdown.core import Markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


class ImageCaptionExtension(Extension):
    def __init__(self, configs: dict[str, Any] | None = None) -> None:
        if configs is None:
            configs = {}
        super().__init__(**configs)

    def extendMarkdown(self, md: Markdown) -> None:
        image_caption = ImageCaptionTreeprocessor(md)
        image_caption.config = self.getConfigs()
        md.treeprocessors.register(image_caption, "imagecaption", 0)
        md.registerExtension(self)


class ImageCaptionTreeprocessor(Treeprocessor):
    def run(self, root: ElementTree.Element) -> None:
        for i, p in enumerate(list(root)):
            if p.tag == "img" and "alt" in p.attrib:
                elem = root.makeelement("figure", {})
                root[i] = elem
                elem.append(p)
                caption = ElementTree.SubElement(elem, "figcaption")
                caption.text = p.attrib["alt"]
            self.run(p)


def makeExtension(configs: dict[str, Any] | None = None) -> ImageCaptionExtension:
    return ImageCaptionExtension(configs=configs)
