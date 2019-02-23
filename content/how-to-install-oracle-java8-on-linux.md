Title: How to install Oracle Java 8 on Linux
Date: 23-03-2014
Slug: how-to-install-oracle-java8-on-linux
Category: Linux
Tags: Linux, Java

Recently I wrote a post [How to install Oracle Java on Fedora Linux](/how-to-install-oracle-java-on-fedora-linux.html).
In this tutorial I will explain you how to install the latest version of Oracle Java on Linux systems.

[Download Java
8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
from Oracle's website:

For 32bit users:

```
wget --no-check-certificate --no-cookies - --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8-b132/jdk-8-linux-i586.tar.gz
```
For 64bit users:

```
wget --no-check-certificate --no-cookies - --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8-b132/jdk-8-linux-x64.tar.gz</code>
```

Unpack the downloaded jdk archive in **/opt/java** directory:

For 32bit users:

```
mkdir /opt/java
tar xzvf jdk-8-linux-i586.tar.gz -C /opt/java
```

For 64bit users:

```
mkdir /opt/java
tar xzvf jdk-8-linux-x64.tar.gz -C /opt/java
```

Install java, javaws, libjavaplugin.so (Java plugin for Firefox), javac and jar:

For 32bit users:

```
java=/opt/java/jdk1.8.0
update-alternatives --install /usr/bin/java java ${java}/bin/java 20000
update-alternatives --install /usr/bin/javaws javaws ${java}/bin/javaws 20000
update-alternatives --install /usr/lib/mozilla/plugins/libjavaplugin.so libjavaplugin.so ${java}/jre/lib/i386/libnpjp2.so 200000
update-alternatives --install /usr/bin/javac javac ${java}/bin/javac 20000
update-alternatives --install /usr/bin/jar jar ${java}/bin/jar 20000
```

For 64bit users:

```
java=/opt/java/jdk1.8.0
update-alternatives --install /usr/bin/java java ${java}/bin/java 20000
update-alternatives --install /usr/bin/javaws javaws ${java}/bin/javaws 20000
update-alternatives --install /usr/lib64/mozilla/plugins/libjavaplugin.so libjavaplugin.so.x86_64 ${java}/jre/lib/amd64/libnpjp2.so 200000
update-alternatives --install /usr/bin/javac javac ${java}/bin/javac 20000
update-alternatives --install /usr/bin/jar jar ${java}/bin/jar 20000
```

Choose which Java will be used as default:

```
update-alternatives --config java
```

Check which Java version is in use:

```
java -version
```
