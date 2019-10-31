Title: How to install Python from source on Debian GNU/Linux
Slug: how-to-install-python-from-source-on-debian-gnu-linux
Date: 31-10-2019
Category: Linux
Tags: Python, Debian, Linux, Installation

The default Python 3 version on Debian is 3.7, and the latest Python release
is 3.8.

To install the latest Python version, you need to compile it from source code.

Before compilation process, first you need to install a few required tools and
dependences needed for building Python from source.

```
$ sudo apt install build-essential wget libssl-dev zlib1g-dev libbz2-dev liblzma-dev libffi-dev tcl-dev libgdbm-dev libsqlite3-dev libreadline-dev tk tk-dev libmpdec-dev
```

Next, download the latest Python release from [python.org web site](https://www.python.org/downloads/source/ "Python.org"):

```
$ wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
```

Verify and unpack the downloaded archive file:

```
$ md5sum xvzf Python-3.8.0.tgz
e18a9d1a0a6d858b9787e03fc6fdaa20  Python-3.8.0.tgz

$ tar xvzf Python-3.8.0.tgz
```

The next step is to run the configure command to prepare the build:

```
$ cd Python-3.8.0

$ ./configure --enable-loadable-sqlite-extensions --enable-shared --with-lto --enable-optimizations --with-system-expat --with-system-ffi --with-computed-gotos --with-system-libmpdec --enable-ipv6 CC=x86_64-linux-gnu-gcc
```

> Use **--with-pydebug** flag if you want to build Python with debug info
>
> Use **--with-dbmliborder=bdb:gdbm** flag if you want to build Python
> with DBM Module against Berkeley DB (GDBM)

After the *configure* script finishes its job, you can build Python using the
`make` command:

```
$ make -j 8
```

Replace 8 with the number of cores that your CPU have.

```
$ grep -c processor /proc/cpuinfo
8
```

When the compilation process finishes, in order to install Python, use the
following command:

```
$ sudo make altinstall
```

> We use the `make altinstall` instead of the `make install` command, because
> we don't want to overwrite our system python installation.

The new Python executable will be installed in */usr/local/bin* directory. You
can run it executing the `python3.8` command in your terminal:

```python
$ python3.8

Python 3.8.0 (default, Oct 15 2019, 10:08:48)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import sysconfig
>>>
>>> sysconfig.get_python_version()
'3.8'
>>>
>>> sysconfig.get_path('stdlib')
'/usr/local/lib/python3.8'
>>>
>>> sysconfig.get_platform()
'linux-x86_64'
>>>
sysconfig.get_config_var('CONFIG_ARGS')
"'--enable-loadable-sqlite-extensions' '--enable-shared' '--with-lto' '--enable-optimizations' '--with-system-expat' '--with-system-ffi' '--with-computed-gotos' '--with-system-libmpdec' '--enable-ipv6' 'CC=x86_64-linux-gnu-gcc'"
```

If python complains that can not load the shared library
**libpython3.8.so.1.0**, you'll need to create a symbolic link to the
*/usr/local/lib/libpython3.8.so.1.0* library:

```
$ sudo ln -s /usr/local/lib/libpython3.8.so.1.0 /usr/lib/libpython3.8.so.1.0
```

Then, verify that the library is properly loaded:

```
$ ldd /usr/local/bin/python3.8
libpython3.8.so.1.0 => /usr/local/lib/libpython3.8.so.1.0 (0x00007fae8b790000)
```

