# zoek
Searchtool for packages: look for both native, flatpak and snap packages at the same time
    
*Search for native, flatpak and snap packages with one command. Run this script with the search string as argurment*

Works with my favorite Linux distributions: 
* [Solus](https://getsol.us)
* Debian, Ubuntu & other Debian derivates
* Arch
* CentOS, Redhat, Fedora
    
    <!--- just 
![screenshot](https://i.imgur.com/9Xo6C82.png) 
---> 
[![asciicast](https://asciinema.org/a/7G2axyCL0PX32ENQKAbOEjt6i.svg)](https://asciinema.org/a/7G2axyCL0PX32ENQKAbOEjt6i)
    
instructions:
1. Save the [script](https://github.com/bvdlingen/zoek/blob/master/zoek) as **/usr/bin/zoek**
2. Set execute permissions:
```
chmod +x /usr/bin/zoek
```

Dependencies:
* [flatpak](https://flatpak.org/setup/)
* [snap (snapd)](https://snapcraft.io/docs/installing-snapd)
* [lolcat](https://github.com/busyloop/lolcat)
```
sudo gem install lolcat
```
