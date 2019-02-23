Title: How to remove items from Places sidebar in Nautilus file manager?
Slug: how-to-remove-items-from-places-sidebar-in-nautilus
Date: 07-06-2014
Category: Linux
Tags: Nautilus, Gnome, Linux

To remove items from places sidebar in Nautilus, open the **~/.config/user-dirs.dirs** file and remove lines that refer to items you don't want.

```
XDG_DESKTOP_DIR="$HOME/Desktop"
XDG_DOWNLOAD_DIR="$HOME/Downloads"
XDG_PUBLICSHARE_DIR="$HOME/Public"
XDG_DOCUMENTS_DIR="$HOME/Documents"
XDG_MUSIC_DIR="$HOME/Music"
XDG_VIDEOS_DIR="$HOME/Videos"
XDG_PICTURES_DIR="$HOME/Pictures"
```

To make these changes permanent, run the following command in your terminal:

```
echo "enabled=false" > ~/.config/user-dirs.conf
```
