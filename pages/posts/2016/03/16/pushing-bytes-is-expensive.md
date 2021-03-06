title: Pushing bytes is expensive
date: 2016-03-16T16:05:00
tags: [technology, cloud]

In this post I'll be comparing cloud hosting costs, which I'm sure will be hopelessly out of date in just a few months.

I'm writing this post to try to solicit feedback on cheaper file transfer options.  If you have any advice or feedback, I'd love to hear about it!

Maybe it should have been obvious, but I've been somewhat surprised at the high cost of transfer vs. storage when you start talking 10s of terabytes.

For example, storing 10TB of data in S3: $302.60, transferring 10TB of data out of S3: $921.51.

I've also been (pleasantly) surprised at how aggressive the AWS/CloudFront (CDN) pricing is -- at $0.085/GB (US only), it appears to be the cheapest way to get data out of AWS.  It's cheaper than both S3 directly ($0.09) and even cheaper than serving directly from an EC2 instance (also $0.09).  This is kind of amazing considering all the benefits of the CF service vs. doing it yourself, or even S3.

I've been working out the details for a SaaS app that doesn't use a lot of storage, but has the potential to have a lot of subscribers.  So, it will use say 200MB of storage, but need to serve that data potentially 50,000 times each month.  The S3 costs are neglible, a few cents, but even the cheapeast CF tier (US only), we are talking $870.40/month.

I love the CloudFront feature set and service and will continue to use it where it makes sense.

For this app, I will have a hard time being competitive with other apps in this space with those costs, so I've been looking for cheaper solutions.  Below is a list of what I've compiled.  I'm not considering any "free tiers" for the comparison.  These are great for development/etc., but I think not relevant in an ongoing cost comparison.

<table class="table">
  <tr><th>Provider</th><th>Transfer Cost/GB</th></tr>

  <tr><td>AWS/CloudFront (US)</td><td><a href="https://aws.amazon.com/cloudfront/pricing/">$0.085</a></td></tr>
  <tr><td>AWS/S3 (us-east)</td><td><a href="https://aws.amazon.com/s3/pricing/">$0.09</a></td></tr>
  <tr><td>AWS/EC2</td><td><a href="https://aws.amazon.com/ec2/pricing/">$0.09</a></td></tr>

  <tr><td>Google Cloud Storage</td><td><a href="https://cloud.google.com/storage/pricing">$0.12</a></td></tr>
  <tr><td>BackBlaze/B2</td><td><a href="https://www.backblaze.com/b2/cloud-storage-pricing.html">$0.05</a></td></tr>
</table>


### Other Options
#### CloudFlare

CloudFlare is a pretty full featured CDN that actually even offers a "free" tier.

I signed up for a "pro" account to test it out.  The problem is that even for the pro and business levels, there's absolutely no record provided of file access.  That requires an Enterprise/Custom plan, where the pricing is determined by the sales team.  I haven't yet made a call to a sales rep to determine what final pricing would be for my use case.

The other tricky thing here is that I still need to separately maintain and pay for an origin, the costs of which are entirely determined by how effectively CloudFlare can cache my content.  What I mean is, if I put CloudFlare in front of CloudFront, and I'm only getting 50% hit rate from CloudFlare, I'm still paying for $435/month from CloudFront on top of what I'm paying from CloudFlare (that's a lot of CFs).

#### Digital Ocean

From what I can tell, they don't offer a straight cloud storage solution, but their "Most Popular" plan features 3TB of data transfer included for $20/month.

This works out to $0.00666/GB.  Of course, I would like some basic redudency, so, say two machines and a load balancer, works out to about $0.01/GB/month? (($20*3)/6000), which is by far the cheapest I've seen.

Of course, there's quite a bit more there to build and manage.

#### Reserved/Custom CloudFront pricing

The [CloudFront pricing page](https://aws.amazon.com/cloudfront/pricing/) does mention that you can reach out for reserved pricing if you commit to 10TB/month for a year.

### Requirements

- Must be within the provider's ToS to support file distribution
  - In searching for options, I've seen a few "Unlimited" or "Unmetered" options, but if you look at the fine print, they're not meant for file storage/distribution, and that's not allowed.
- Reasonable file serving redundancy
  - I'd like to avoid a single machine for file serving.  I'll probably use S3 as the "source of truth", but I want to avoid downtime in file serving.
- Access logs available
  - I need to be able to compile basic download stats on files served (apache style logs or similar).

## Please Send Feedback/Suggestions!

Again, I'm looking for feedback and suggestions for a cheap, reliable file hosting provider.

Thanks!
