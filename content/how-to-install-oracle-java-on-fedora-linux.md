Title: How to install Oracle Java on Fedora Linux
Slug: how-to-install-oracle-java-on-fedora-linux
Date: 15-03-2014
Category: Linux
Tags: Linux, Fedora, Java

To install Oracle Java on Fedora/CentOS Linux, open the Terminal and follow the
next steps:

First, change to root user:

```
su
```

or

```
sudo su
```

Next, Download Oracle Java [jdk](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)
and
[jre](http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html) packages:

For 32bit users:

```
wget -c --no-cookies --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com" "http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-i586.rpm" "http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jre-7u51-linux-i586.rpm"
```

For 64bit users:

```
wget -c --no-cookies --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com" "http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm" "http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jre-7u51-linux-x64.rpm"
```

Install downloaded packages:

```
yum -y install *.rpm
```

Set up java, javaws, libjavaplugin.so (Java plugin for Firefox) and javac:

For 32bit users:

```
alternatives --install /usr/bin/java java /usr/java/latest/jre/bin/java 200000
alternatives --install /usr/bin/javaws javaws /usr/java/latest/jre/bin/javaws 200000
alternatives --install /usr/lib/mozilla/plugins/libjavaplugin.so libjavaplugin.so /usr/java/latest/jre/lib/i386/libnpjp2.so 200000
alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 200000
alternatives --install /usr/bin/jar jar /usr/java/latest/bin/jar 200000
```

For 64bit users:

```
alternatives --install /usr/bin/java java /usr/java/latest/jre/bin/java 200000
alternatives --install /usr/bin/javaws javaws /usr/java/latest/jre/bin/javaws 200000
alternatives --install /usr/lib64/mozilla/plugins/libjavaplugin.so libjavaplugin.so.x86_64 /usr/java/latest/jre/lib/amd64/libnpjp2.so 200000
alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 200000
alternatives --install /usr/bin/jar jar /usr/java/latest/bin/jar 200000
```

Check if Java is installed:

```
java -version
```

Also, I wrote [this little bash script](https://dl.dropboxusercontent.com/u/9196683/Fedora/java-install.sh)
that allows you to install Oracle Java with a single command in Terminal.
All you need to do is to run a script as root user:

```
sh java-install.sh
```
