title: New Photo Portfolio Site
date: 2016-01-09T16:37:00
tags: [photography]
photo: https://photos.ogrodnek.com/static/photos/postcards-seattle/women-pier-thumb-375x375.jpg

![](https://photos.ogrodnek.com/static/photos/postcards-seattle/women-pier-thumb-375x375.jpg)

I still post new photos to [my account on Flickr](https://www.flickr.com/photos/logrodnek/), but I've been wanting
to put together a site with an organized, curated set of my favorite photos.

I finally got around to it: [photos.ogrodnek.com](https://photos.ogrodnek.com)

I wanted it to be clean, simple, look good on mobile, and FAST, and I think I'm off to a pretty good start.

## tech

I went back and forth between building my own thing and using a portfolio site, and of course I ended up building my own thing.

I used [Cactus](http://cactusformac.com/) to do the templating and generate the static site content, which is deployed to S3 and uses CloudFront as the CDN.

You can see the source and scripts that ends up generating the site here: [https://github.com/ogrodnek/photos.ogrodnek.com](https://github.com/ogrodnek/photos.ogrodnek.com)

### Cactus

So far I like it... I've tried a bunch of other static site generators and I think Cactus fits with me the best so far.  Unfortunately, it's not that well documented.

### CloudFront

I love CloudFront!  It really makes serving content like this so much faster.  The new support for gzip compression is a huge help.  For personal sites like this, it's also pretty easy to fit comfortably within the free usage tier.

I don't yet have a good/automated setup for doing cache invalidaton yet, or for setting cache expiration headers.  I think the newer version of cactus does have a plugin for doing asset fingerprinting to generate unique infinitely cachable names, which would definitely help.

