Title: How to change DNS Name Servers in Linux?
Slug: how-to-change-dns-name-servers-in-linux
Date: 23-04-2013
Category: Linux
Tags: Linux, DNS

The file to change DNS nameservers in Linux is **/etc/resolv.conf**:

```
cat /etc/resolv.conf
```

For example, if you want to set up [Google public DNS](http://code.google.com/speed/public-dns/), open the file:

```
sudo nano /etc/resolv.conf
```

And add the following lines:

```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

Save the changes with *Ctrl+O* and Enter, then *Ctrl+X* to exit from nano editor.

Restart the network:

```
sudo /etc/init.d/networking restart
```

Or, in Network Manager, go to *Edit->IPv4 Settings* tab, choose *Automatic
(DHCP) addresses only* and add DNS IP addresses.
