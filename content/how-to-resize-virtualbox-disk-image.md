Title: How to resize a VirtualBox disk image?
Slug: how-to-resize-virtualbox-disk-image
Date: 29-08-2013
Category: HowTo
Tags: VirtualBox

To resize a VirtualBox disk image (VDI), go to the directory where the .vdi file
is located, it's usually in **~/VirtualBox VMs**, and run the following command:

```
VBoxManage modifyhd file.vdi --resize SizeInMB
```

For example:

```
VBoxManage modifyhd Ubuntu.vdi --resize 20000
```

The command will resize VDI to 20 GB, or more precisely 19.53 GB.
