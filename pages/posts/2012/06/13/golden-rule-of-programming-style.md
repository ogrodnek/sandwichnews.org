title: The golden rule of programming style
date: 2012-06-13T12:00:00
tags: [technology,feedback,code,programming]

There's an interesting page on the subject of [compilation units per file](http://docs.scala-lang.org/style/files.html) over at the 
[scala style guide](http://docs.scala-lang.org/style/overview.html). 


The guideline, is, delightfully vague, which I will paraphrase as: 
Mostly use single files, unless you can't, or unless it's better if you don't. 

The author(s) go on to expand on the reasoning behind breaking the guideline:

> Another case is when multiple classes logically form a single, cohesive group, sharing concepts to the point where maintenance is greatly served by containing them within a single file. These situations are harder to predict…  Generally speaking, if it is easier to perform long-term maintenance and development on several units in a single file rather than spread across multiple, then such an organizational strategy should be preferred for these classes.
 
This touches on what I consider to be the golden rule of programming style: <strong>Make your intent clear and the code easy to read.</strong> 

Software spends most of its life in maintenance, which is why we have style guides and coding standards.  It's valuable to have consistent looking code to promote a shared vocabulary, improve readability, and steer away from confusing or error-prone constructs. 

It is just as important to be able to understand, both as an author and as a reviewer, that in certain cases following the letter of the law goes against the main goal of improving readability and maintenance.  A one-size-fits-all rule does not always work, and as the authors of this particular guideline mention, "these situations are harder to predict." 

### Make your intent clear and the code easy to read.

