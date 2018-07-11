import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code']

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


for p in pages:
  print p.meta


@app.route('/')
def index():
    tags = set()
    for p in pages:
      for t in p.meta.get('tags', []):
        tags.add(t)
    
    _s = sorted(tags)

    latest = sorted(pages, reverse=True, key=lambda p: str(p.meta['date']))
    return render_template('index.html', pages=latest, tags=_s)


@app.route('/rss.xml')
def rss():
  latest = sorted(pages, reverse=True, key=lambda p: str(p.meta['date']))
  return render_template('rss.xml', posts=latest), 200, { 'Content-Type' : "application/xml" }

@app.route('/tag/<string:tag>/')
def tag(tag):
    _tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    tagged = sorted(_tagged, key=lambda p: p.meta['date'], reverse=True)

    return render_template('tag.html', pages=tagged, tag=tag)

def related(page):
  def find():
    rel = {}
    for p in pages:
      if p.path == page.path:
        continue
      for t in page.meta.get('tags', []):
        if t in p.meta.get('tags', []):
          rel[p.path] = p
    return rel
  
  rel = find().values()

  return sorted(rel, key=lambda p: p.meta['date'], reverse=True)

@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    r = related(page)

    return render_template('page.html', page=page, related=r)

if __name__ == '__main__':
    if len(sys.argv) > 1 and (sys.argv[1] == "build" or sys.argv[1] == "freeze"):
        freezer.freeze()
    else:
        app.run(port=8000)