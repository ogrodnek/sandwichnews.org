title: Office River Timelapse
date: 2025-12-04T18:24:34
tags: [technology, timelapse, river, aws, photography]
photo: /static/images/posts/2025/12/04/river-timelapse.jpeg

I was wondering why one of my AWS accounts had almost 1TB of data in S3. Turns out I never cleaned up the images from [Shipping News](https://shippingnews.xyz/about) -- a project where I captured a photo every 30 seconds from my office window, saved it to S3, and ran image recognition to detect boats passing by on the Hudson.

I've been doing a lot with [ffmpeg](https://ffmpeg.org/) lately, so I thought I'd see if I could make a quick timelapse. This is just the first day I captured, but I think I have about a year of data...

<video src="/static/images/posts/2025/12/04/timelapse_2022-08-13_web_1080p.mp4" title="Hudson River Window Aug 13, 2022" controls></video>

It's been offline for a couple years now. I started getting lots of false positives, so I "temporarily" turned it off.

I've still been meaning to take the images with detected boats and try some labeling/training with <a href="https://pjreddie.com/darknet/yolo/">YOLO</a>.  I'd love to bring it back online if I can get more reliable detection.

It would be cool to do a full year timelapse with detection -- slowing down when boats are crossing the screen, and speeding up when not much is happening.

This is what makes me a digital hoarder. Now I'm never going to be able to delete these images!
