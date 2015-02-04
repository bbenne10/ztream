## ztream - A mplayer/mpv streamer 'controller' script written in Z-shell.

ztream was written as a small excercise in learning shell mechanics. I intended
for it to be POSIX-compliant, but the associative array data structure made
z-shell MUCH more appealing.

You can configure some of the behavior by modifying the global variables above
the 'fold'.

#### INSTALLATION:
* Install mpv and dmenu (or mplayer and dmenu, though mplayer is largely untested)
* Install ZSH (any relatively recent version should work. If not, please open a ticket)
* Modify the associative array of Station name to url (and any other configurables)
* Put ztream in your `$PATH`
* `./ztream` (or put it in your sxhkdrc, or dwm's config.h or whatever)

#### NOTES:
Earlier versions of ztream allowed specifying the action as the first and only
argument. This is no longer possible as all args are sent along to dmenu.

#### TODO:
??? I have no new ideas yet...
