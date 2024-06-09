# 0x19. Postmortem
**DevOps SysAdmin**

![]()

## Issue Summary

Our recently launched Airbnb clone website experienced a critical issue following a new feature deployment. 10 minutes after the update, users reported being unable to book guest houses and hotel services on our platform. We received significant number of  user complaints, impacting for about 45% of our users. Further investigation revealed a misconfigured database connection pool. This configuration error prevented the application from establishing a stable connection to the database, hindering user authentication and booking processes. The malfunction began On 09-06-2024, at 4:20 PM GMT+3 and persisted until the database connection pool was rectified On 09-06-2024, at 11:10 PM GMT+3. This incident highlights the importance of thorough configuration management and automated testing procedures, particularly after deployments.

## Timeline

+ 09-06-2024 4:20 PM GMT+3 - The issue began. User reports indicated an inability to complete bookings.
+ 09-06-2024 4:20 PM GMT+3 - Mahari, our backend sinor developers, experienced the same issues our customers reported.
+ 09-06-2024 4:30 PM GMT+3 - Engineering team investigates the issue. Initial troubleshooting focuses on database logs, query performance and network connectivity.
+ 09-06-2024 4:40 PM GMT+3 - They identify the database connection failure and begin troubleshooting the database server.
+ 09-06-2024 4:45 PM GMT+3 - We were mislead by thinking that the  external API for availability verification experienced an outage.
+ 09-06-2024 4:50 PM GMT+3 - The incident was escalated incident to the DevOps team..
+ 09-06-2024 5:00 PM GMT+3 - The team restarts the database server, which resolves the connection issue.
+ 09-06-2024 5:10 PM GMT+3 -  Functionality is verified, and the incident is declared resolved.

## Root Cause And Resolution

The root cause of the outage was a failure of the connection between the web application and the database. The engineering team identified the issue through monitoring alerts and successfully resolved it by restarting the database server.

## Corrective And Preventative Measures

+ Investigate the cause of the database server failure. This may involve reviewing server logs or performing further diagnostics.
+ Setup a monitoring system for the database and application servers to keep track of any issue that may occur.
+ Improve monitoring of the database server health to provide early warnings of potential issues.
+ Implement automated failover mechanisms to ensure the application can connect to a secondary database in case of a primary server failure.
