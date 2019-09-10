#!/bin/bash
echo "Content-type: text/html"
echo
/usr/bin/sudo -n -S /sbin/shutdown -P +0 2>&1 && echo "Poweroff is scheduled" || echo "Failed to switch the server off"
