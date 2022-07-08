title: hackday - analog meters
date: 2010-08-13T10:00:00
tags: [technology, electronics]

For this last hackday, I decided to work on something more hardware hacking related. At this year's [Maker Fair](https://makerfaire.com/), I was really inspired by all the cool stuff people were building, so I picked up an [arduino](https://www.arduino.cc/) and started playing around with a couple of things.

I've always wanted to have some cool old-school analog VU type meters displaying web requests.

Here's my completed hackday project:

<img src="http://farm5.static.flickr.com/4073/4886748674_69d378a309.jpg" />

Here's a view of the components from the back:

<img src="http://farm5.static.flickr.com/4096/4886751606_76ebe9ed1c.jpg" />

It's battery operated and receives data wirelessly over RF from another arduino I have hooked up via serial to my laptop.

It's pretty simple, but I'm still totally psyched about how it came out.

The main components are some analog panel meters (kinda pricey, but awesome), and an RF receiver. The frame is a piece of scrap acrylic from TAP Plastics that I drilled and cut to size, and the stand is a piece of a wire clothes hanger bent to shape.

Connected to my computer is a another arduino (actually a [volksduino](http://www.appliedplatonics.com/volksduino/)) that receives updates over USB and sends the data out over RF:

<img src="http://farm5.static.flickr.com/4142/4886752598_2522c0839b_d.jpg" />

You may be asking, why bother with wireless if you need a computer hooked up through serial anyway. Or you may ask why not just connect to a wireless network directly.

Well, I wanted the meters to be able to be moved around, or mounted on a wall... I wanted them wireless. But, it turns out that wireless and even ethernet solutions for connecting an arduino to the internet directly are comparatively pretty expensive. Even using bluetooth is expensive. My long term plan is to have a single arduino connected to the internet directly (via ethernet or wireless), and have it serve as a proxy over RF for the others... So this is a bit of work towards that.

I wrote a bit of Java code to connect to amazon's cloudwatch to pull the load balancer statistics for two of our services. I then discovered it's near impossible to connect to anything over USB in Java... It is ridiculous. Luckily, it's REALLY easy to do this with [Processing](https://processing.org/), so I wrote a simple processing program that used my cloudwatch library and wrote it out to serial.

And that's really it. The arduino reads data over serial, and periodically sends it over RF. The arduino hooked up to the meters simply reads the values over RF and sets the meters to display a scaled version of the results. They're showing requests per second. We get a huge amount of requests per second with these services, so the numbers on the dial aren't actually correct (I need to make some custom faceplates). It also flashes an LED every time it gets a RF transmission.

Here's a quick video of it in action:

The one thing I'm not crazy about is that the maximum resolution you can get from cloudwatch is stats per minute, so the meters don't actually change as often as I would like.

Still, pretty cool. I'm looking forward to building some more displays like this in the future.
