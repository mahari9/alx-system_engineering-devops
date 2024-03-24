# Simple Web Stack


[Visit Board](https://imgur.com/apCX7uR)

## Description

This is a one server web infrastructure that hosts a website that is reachable via `www.foobar.com`. With no firewalls or SSL certificates for protecting the server's network. Each component (database, application server) has to share the resources like CPU, RAM, and SSD provided by the server.

## Specifics About Infrastructure

+ What a server is.<br/>A server is A server is a specialized computer or software system designed to provide services, data, or resources to other computers, known as
clients, over a network.

+ The role of the domain name.<br/> a domain name serves as a human-friendly label that maps to specific Internet resources, such as websites or email services. It provides ownership, credibility, and brand identity, making it easier for users to access online content. Remember The IP address and domain name alias is mapped in the Domain Name System (DNS).

+ The type of DNS record `www` is in `www.foobar.com`.<br/>`www.foobar.com` uses an **A record**. This can be checked by running `dig www.foobar.com`.<br/>**Note:** the results might be different but for the infrastructure in this design, an **A** record is used.<br/>

+ The role of the web server.<br/>The web server is a software/hardware that accepts requests via HTTP or secure HTTP (HTTPS) and responds with the content of the requested resource or an error messsage.

+ The role of the application server.<br/>To install, operate and host applications and associated services for end users, IT services and organizations and facilitates the hosting and delivery of high-end consumer or business applications

+ The role of the database.<br/>To store a collection of organized information that can easily be accessed, managed and updated

+ What the server uses to communicate with the client (computer of the user requesting the website).<br/>Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.

## Issues With This Infrastructure

+ There are multiple SPOF (Single Point Of Failure) in this infrastructure.<br/>Example, if the MySQL database server is down, the entire site would be down.

+ Downtime when maintenance needed.<br/>When we need to run some maintenance checks on any component, they have to be put down or the server has to be turned off. Since there's only one server, the website would be experiencing a downtime.

+ Cannot scale if there's too much incoming traffic.<br/>It would be hard to scale this infrastructure becauses one server contains the required components. The server can quickly run out of resources or slow down when it starts receiving a lot of traffics.
