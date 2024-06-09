# 0x19. Postmortem
**DevOps SysAdmin**

## Concepts
For this project, we expect you to look at this concept:
* [On-call](https://intranet.alxswe.com/concepts/39 "On-call")

# Background Context
![](https://www.youtube.com/watch?v=rp5cVMNmbro&feature=youtu.be)

Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

* To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
* And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

# Resources
**Read or watch:**

* [Incident Report, also referred to as a Postmortem](https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem "Incident Report, also referred to as a Postmortem")
* [The importance of an incident postmortem process](https://www.atlassian.com/incident-management/postmortem "The importance of an incident postmortem process")
* [What is an Incident Postmortem?](https://www.pagerduty.com/resources/learn/incident-postmortem/ "What is an Incident Postmortem?")


## Tasks

![](https://twitter.com/devopsreact/status/834887829486399488)

+ [x] 0. My first postmortem<br/>_**[Blog_Post.md](Blog_Post.md)**_ contains a blog post that meets the following requirements:
  + **INFO:**
    + Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)
    + While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.
  + **Requirements:**
    + Issue Summary (that is often what executives will read) must contain:
      + Duration of the outage with start and end times (including timezone).
      + What was the impact? (What service was down/slow? What were user experiencing? How many % of the users were affected?)
      + What was the root cause?
    + Timeline (format bullet point, format: `time` - `keep it short, 1 or 2 sentences`) must contain:
      + When was the issue detected?
      + How was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
      + Actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue).
      + Misleading investigation/debugging paths that were taken.
      + Which team/individuals was the incident escalated to?
      + How the incident was resolved.
    + Root cause and resolution must contain:
      + Explain in detail what was causing the issue.
      + Explain in detail how the issue was fixed.
    + Corrective and preventative measures must contain:
      + What are the things that can be improved/fixed (broadly speaking)
      + A list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…).
      + Be brief and straight to the point, between 400 to 600 words

+ [x] 1. Make people want to read your postmortem
  + We are constantly stormed by a quantity of information, it’s tough to get people to read you.
  + Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience attention.
