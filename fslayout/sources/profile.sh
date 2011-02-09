#!/bin/sh
# /etc/profile: This file contains system-wide defaults used by
# all Bourne (and related) shells.

# Set the values for some environment variables:
export MINICOM="-c on"
export MANPATH=/usr/local/man:/usr/man:/usr/X11R6/man
export HOSTNAME=$(< /etc/hostname)
export LESSOPEN="|lesspipe.sh %s"
export LESS="-RM"
export EDITOR=vim

# If the user doesn't have a .inputrc, use the one in /etc.
if [[ ! -r "${HOME}/.inputrc" ]]; then
    export INPUTRC=/etc/inputrc
fi

# Set the default system $PATH:
PATH='/bin:/usr/bin:/usr/local/bin:/opt/games:/usr/games:.'

# For root users, ensure that /usr/local/sbin, /usr/sbin, and /sbin are in
# the $PATH.  Some means of connection don't add these by default (sshd comes
# to mind).
if [[ "$(id -u)" -eq 0 ]]; then
    PATH="/sbin:/usr/sbin:/usr/local/sbin:${PATH}"
fi

# I had problems using 'eval tset' instead of 'TERM=', but you might want to 
# try it anyway. I think with the right /etc/termcap it would work great.
# eval `tset -sQ "$TERM"`
if [[ "$TERM" = "" || "$TERM" = "unknown" ]]; then
    export TERM=linux
fi

# Set a default shell prompt:
export PS1='\u@\h:\w\$ '
export PS2='> '

# Default umask.  A umask of 022 prevents new files from being created group
# and world writable.
umask 022

# Set up the LS_COLORS and LS_OPTIONS environment variables for color ls:
eval $(dircolors --sh)

# Notify user of incoming mail.  This can be overridden in the user's
# local startup file (~/.bash.login or whatever, depending on the shell)
export MAILPATH=~/Maildir
export MAILCHECK=60

# Append any additional sh scripts found in /etc/profile.d/:
for file in /etc/profile.d/*.sh
do
	if [[ -x "$file" ]]; then
        . "$file"
    fi
done
