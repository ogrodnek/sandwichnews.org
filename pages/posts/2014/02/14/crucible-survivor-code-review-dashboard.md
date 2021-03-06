title: Crucible Survivor - a code review dashboard
author: larry ogrodnek
date: 2014-02-14T10:15:00
tags: [technology, code, scala]
photo: https://raw.github.com/ogrodnek/crucible-survivor/master/docs/crucible-survivor-small.png

![Crucible Survivor Dashboard](https://raw.github.com/ogrodnek/crucible-survivor/master/docs/crucible-survivor-small.png)

  I've talked a lot about the importance of [code reviews and developer feedback]()
  
  [Crucible Survivor](https://github.com/ogrodnek/crucible-survivor) is a Hall of Fame / Hall of Shame dashboard that helps to encourage completing your reviews.
  
  It integrates with with [Crucible](https://www.atlassian.com/software/crucible/overview) (obviously) for code review stats.
  
## Scoring

  The scoring is pretty simple right now.  Each reviewer gets a *Fame* point for completing a review, and a *Shame* point for each review they have not yet completed.
  
  We've had this running for a few months now, and the general thinking is it would be better to have open reviews be more shameful the longer they have been kept open.  Maybe a future improvement.
  

## Design / Credits
 
 The design is taken from [Jira Survivor](http://blog.gengo.com/jira-survivor/), which itself was forked from [Github Survivor](http://99designs.com/tech-blog/blog/2013/01/05/github-survivor/).
 
## Code and Application Architecture

  The [code](https://github.com/ogrodnek/crucible-survivor) is a large departure from the original projects.  The original projects use MongoDB to store data scraped from the github/jira APIs, and a python web app to serve the site.

  Crucible Survivor is an angular app that is mostly static.  The review stats are included in the app as a JS include.  The app is hosted as a static website in S3, with the contents of the stats JS generated periodically by a jenkins server.

  This was a hack-day experiment in 'static' dashboard apps, and I'm really happy with how it came out.  I really like how gathering the content to display is decoupled from the display.  Serving the site requires no server infrastructure, and the update process can be very flexible.  Finally, it's incredible easy to test/run locally -- just generate a fake stats file and open the site.
  
### Grab the code, get it running!

  The code is [open sourced, and available on github](https://github.com/ogrodnek/crucible-survivor) along with instructions on configuring, running, developing.
  
  I'd love to hear any feedback or comments.
  
