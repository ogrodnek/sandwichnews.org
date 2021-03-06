title: On Code Reviews and Developer Feedback
date: 2012-03-13T12:00:00
tags: [technology,feedback,code,programming]

There's a great post from last week at 37signals, [Give it five minutes](http://37signals.com/svn/posts/3124-give-it-five-minutes):

> While he was making his points on stage, I was taking an inventory of the things I didn’t agree with. 
> And when presented with an opportunity to speak with him, I quickly pushed back at some of his ideas. I must have seemed like such an asshole. 
>
>
> His response changed my life. It was a simple thing. He said “Man, give it five minutes.” I asked him what he meant by that? He said, it’s fine to disagree, 
> it’s fine to push back, it’s great to have strong opinions and beliefs, but give my ideas some time to set in before you’re sure you want to argue against them. 
> “Five minutes” represented “think”, not react. He was totally right. I came into the discussion looking to prove something, not learn something. 
>
>
> There’s also a difference between asking questions and pushing back. Pushing back means you already think you know. Asking questions means you want to know. Ask more questions.
 
This is such a great outlook and a great way to approach the discussion of feedback for code reviews and design reviews. 


It's surprising how little time development teams devote to training, or even internal discussion on effective feedback.  As developers, we are constantly engaged in this kind of communication: white-boarding sessions, spec reviews, design reviews, code reviews.  We're expected to give and receive feedback on a daily basis, but few of us are properly prepared for it.  Not only do we lack the training, but we have many negative examples to draw from.  Who hasn't been a part of a design review where tempers flare?  Properly giving feedback is something that requires constant attention and practice.  Receiving feedback can be just as difficult. 

### Culture of Communication
 
One of the major pillars of our 
[engineering culture at bizo]() is "the 3 Cs": Communication, Communication, Communication. 

We've tried hard to build a team of engineers that are eager to receive feedback, humble about their abilities, objective and gracious with their feedback, and freely giving of their own knowledge and experience.  We see communication as a prerequisite for building a world-class team and developing high-quality code. You often hear the phrase "
[strong opinions, weakly held](http://bobsutton.typepad.com/my_weblog/2006/07/strong_opinions.html)," and that is the kind of culture we have tried to build. 

Communication is hard.  It takes real team agreement and commitment to continued work to keep this culture alive and well. It's important the team views effective communication as important and that the culture supports it. 

### Code Reviews
 
Code reviews are something that can easily be approached from the wrong perspective, both as an author or reviewer. 

As a reviewer, it can be easy to jump in and argue, to try and push 'your' solution (even though it may be equivalent), to push back instead of asking questions and trying to understand. 

As an author, it's far too easy to get attached to your code, to your specific solution/naming/etc.  It's also easy to feel like each comment is an attack on your ability, and that by accepting the feedback, this somehow means that you were wrong or did a bad job.  Of course, nothing could be further from the truth! 

At Bizo, we perform code reviews for every change.  They are a major part of our culture of communication.  In order to perform effective code reviews, it's important to have some shared guidelines that help support effective communication. 

Here are some guidelines we've found to be helpful for performing code reviews: 

### What is a code review

* A careful line-by-line critique of code by peers
  
* Happens in a non-threatening context
  
* Goal is cooperation and mutual learning, not fault finding

Code reviews are a team exercise to improve understanding and make the code better! 

When people think of code reviews they usually think of catching bugs.  Code reviews do occasionally catch bugs or potential performance problems, but this is rare.

Just as important is fostering a shared understanding of the code and exposure to new approaches, techniques, and patterns.  Seeing how your peers program is a great way to learn from them.

Ensuring coding standards and style guides is another way code reviews help.  Working on a team it's important to keep readability and quality high using a shared vocabulary. 

#### As an author

As an author, it's important to view each comment as a new opportunity to improve your code.  Instead of jumping into defense mode, take a step back and think.  Try to approach the code again for the first time with this new perspective.  Your team has a lot of experience and varied backgrounds -- draw from them!  They are there to help you.  Use the gift of their experience and knowledge to improve the code.

Trust the team, and view all comments as action items.  Some changes can seem arbitrary, especially when it comes to naming and organization.  Unless there's a strong reason, tend to agree with your reviewers.  If a reviewer finds something confusing, it is confusing!  Code spends most of its life in maintenance and programming is a team sport.  Remember that they are your audience, and you want them to be able to understand your code at 4am after a system crash. 


#### As a reviewer

As a reviewer, it's important to take the time to understand the code, think, and ask questions to understand the code before providing feedback.  The author probably spent a lot more time thinking about the problem and the approach over the course of the project.

Be strict on coding standard and style guide violations.  The real cost of software is maintenance (
[80% according to Sun](http://www.oracle.com/technetwork/java/javase/documentation/codeconventions-139411.html#16712)).  It's important the code is easily understood by the team.

Be gentle on personal preferences.  If it's not a standard violation and just a matter of personal preference, defer to the author.  It's okay to present your perspective, but mention that it's just a preference and not meant to be taken as an action item.

Trust the author.  It's often the case that there are many valid approaches to a problem.  It's great to present alternative approaches and discuss pros/cons of various approaches.  If you see alternative solutions, bring them up!  When discussing alternatives, make sure to listen to the author.  Remember they are the subject matter expert and you are working together on the same team. 

#### It takes work!

Communication is hard!  It's easy to screw-up.  It's easy to go into attack or defense mode when you're passionate about what you're doing.  It's really something we all need to remind ourselves to work on every day.  It's something we need to periodically remind ourselves as a team.  Try to view each review as an opportunity to practice these guidelines.  Just remember to take a step back, think, and ask questions.
