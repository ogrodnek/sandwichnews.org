import re
from typing import Any
from xml.etree import ElementTree

from markdown.core import Markdown
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
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

        video_caption = VideoCaptionPostprocessor(md)
        md.postprocessors.register(video_caption, "videocaption", 0)

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


class VideoCaptionPostprocessor(Postprocessor):
    VIDEO_PATTERN = re.compile(r'<video([^>]*)\stitle="([^"]+)"([^>]*)></video>')

    def run(self, text: str) -> str:
        def replace_video(match: re.Match[str]) -> str:
            before = match.group(1)
            title = match.group(2)
            after = match.group(3)
            return f'<figure><video{before} title="{title}"{after}></video><figcaption>{title}</figcaption></figure>'

        return self.VIDEO_PATTERN.sub(replace_video, text)


def makeExtension(configs: dict[str, Any] | None = None) -> ImageCaptionExtension:
    return ImageCaptionExtension(configs=configs)
