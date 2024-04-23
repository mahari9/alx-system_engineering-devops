0x0C. Web server
================

Concepts
--------

*For this project, students are expected to look at this concept:*

-   [What is a Child Process?](https://alx-intranet.hbtn.io/concepts/110)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

Background Context
------------------

[![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/Screenshot+2017-07-06+19.24.05.png)](https://www.youtube.com/watch?v=AZg4uJkEa-4&feature=youtu.be&hd=1)[](http://savefrom.net/?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DAZg4uJkEa-4%26feature%3Dyoutu.be%26hd%3D1&utm_source=ff&utm_medium=extensions&utm_campaign=link_modifier "Obtenir un lien direct")

In this project, some of the tasks will be graded on 2 aspects:

1.  Is your `web-01` server configured according to requirements
2.  Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port `8080` instead of `80`, I can use `emacs` on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.

But my answer file would contain:

```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu

```

As you can tell, I am not using `emacs` to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an [SRE](https://alx-intranet.hbtn.io/rltoken/9I0WufjKdW3TZA2EVrGnlQ "SRE"), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the `root` user, you do not need to use the `sudo` command.

A good Software Engineer is a [lazy Software Engineer](https://alx-intranet.hbtn.io/rltoken/sRY__axKNHhNW0SVmsUC_A "lazy Software Engineer"). ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

-   start an `ubuntu:16.04` Docker container
-   run your script on it
-   see how it behaves

Check out the Docker concept page for more info about how to manipulate containers.

Resources
---------

**Read or watch**:

-   [How the web works](https://alx-intranet.hbtn.io/rltoken/6TI3HiyFdwrbXWKVF24Gxw "How the web works")
-   [Nginx](https://alx-intranet.hbtn.io/rltoken/vkVMGlaf39j2DWAQWzo6EA "Nginx")
-   [How to Configure Nginx](https://alx-intranet.hbtn.io/rltoken/zKrpVxWuUHVdW4URAjdFbw "How to Configure Nginx")
-   [Child process concept page](https://alx-intranet.hbtn.io/rltoken/Ar18u5sRis1fkvkVgzdcqg "Child process concept page")
-   [Root and sub domain](https://alx-intranet.hbtn.io/rltoken/xi3peVqYl02PfpHHHlCtxQ "Root and sub domain")
-   [HTTP requests](https://alx-intranet.hbtn.io/rltoken/sBrrP4EAmI3NoYjIgZrUhw "HTTP requests")
-   [HTTP redirection](https://alx-intranet.hbtn.io/rltoken/Eaa4ZuKvye941hTkP8VlBQ "HTTP redirection")
-   [Not found HTTP response code](https://alx-intranet.hbtn.io/rltoken/eJSp2QFTY6jqqNtz8OVDEw "Not found HTTP response code")
-   [Logs files on Linux](https://alx-intranet.hbtn.io/rltoken/7WMNY5CWD-CBrxmQrdmfPg "Logs files on Linux")

**For reference:**

-   [RFC 7231 (HTTP/1.1)](https://alx-intranet.hbtn.io/rltoken/BGa6RrS0dnM6EdBGS_ZDUw "RFC 7231 (HTTP/1.1)")
-   [RFC 7540 (HTTP/2)](https://alx-intranet.hbtn.io/rltoken/IZ2fyYn1qNZ9RXXsg5vG1g "RFC 7540 (HTTP/2)")

**man or help**:

-   `scp`
-   `curl`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/EHyxcIwPtD2SzEGRKOnT3g "explain to anyone"), **without the help of Google**:

### General

-   What is the main role of a web server
-   What is a child process
-   Why web servers usually have a parent process and child processes
-   What are the main HTTP requests

### DNS

-   What DNS stands for
-   What is DNS main role

### DNS Record Types

-   `A`
-   `CNAME`
-   `TXT`
-   `MX`

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted on Ubuntu 16.04 LTS
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing
-   You can't use `systemctl` for restarting a process

Quiz questions
--------------

Show

Your servers
------------

| Name         | Username | IP            | State   |
| ------------ | -------- | ------------- | ------- |
| 426036-web-01| `ubuntu` | `52.73.243.18`| running |


## Tasks :page_with_curl:

* **0. Transfer a file to your server**
  * Bash script that transfers a file
  from our client to a server.
  * Accepts four arguments:
    * The path of the file to be transferred.
    * The IP of the server to transfer the file to.
    * The username that `scp` connects with.
    * The path of the SSH privtae key that `scp` uses.
  * `scp` transfers the file to the user home directory `~/`.

* **1. Install nginx web server**
  * Bash script that configures a new Ubuntu machine with Nginx.
  * Nginx listens on port 80.
  * When querying Nginx at its root `/` with a `curl` GET request,
  it returns a page containing the string `Hello World!`.

* **2. Setup a domain name**
  * A text file containing
  the domain name set up for the server.

* **3. Redirection**
  * Bash script that configures a new Ubuntu
  machine with Nginx.
    * The location `/redirect_me` returns a `301 Moved Permanently` redirection
    to another page.

* **4. Not found page 404**
  *Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

* Requirements:
         *The page must return an `HTTP 404 error code`
         * The page must contain the string `Ceci n'est pas une page`
         * Using what you did with 3-redirection, write 4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task
* **5. Install Nginx web server (w/ Puppet)**
  Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying `/redirect_me`.
 * Requirements:
         * Nginx should be listening on port 80
         * When querying Nginx at its `root` / with a `GET` request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
         * The redirection must be a “301 Moved Permanently”
         * Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements


