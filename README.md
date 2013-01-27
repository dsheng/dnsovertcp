DNS over TCP
==========

Transform the local dns udp request to tcp request, thus avoid dns poisoning or hijacking, this converter is also similar to the dnsproxy.

How to install and configuration

1, Install twisted package

	easy_install twisted

   If no easy_install you need to install python-setuptools and python-devel

2, Run dnsovertcp
   
   For Linux

	sudo ./install
	sudo /etc/init.d/dnsovertcp start

   For Mac OS

    sudo ./install.osx
    sudo /usr/local/bin/dns-overtcp start

3, Edit local nameserver to localhost
  
   For linux or mac os,modify /etc/resolv.conf

	nameserver 127.0.0.1

4, How to check if dnsovertcp is working

   Install dns tools(dnsutils for ubuntu,bind-tutils for centos):

	a, dig twitter.com @127.0.0.1
	b, dig +tcp twitter.com @8.8.8.8
	c, dig twitter.com @8.8.8.8

   The result of a and b should be same, if c is different from others, that means your upstream dns-server is poisoning.

Under MIT license        
