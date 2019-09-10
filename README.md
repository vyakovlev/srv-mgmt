# Server management routines
Tools I use to automate routine tasks on my local server


# My regular tasks and proposed solutions
### No need to be always on (e.g. let's save electricity and extend life of hardware)
I have a Linux server that is used to share our family photo and video archives to local devices. We used to have it 
always on earlier, but it consumes so much power and is so noisy, so I began to looking for options to keep it live only
 when needed.
 
 So basically I wanted an easy and convenient way to start/stop my server when needed.
 
 I also read about Pythonista, that interprets Python code on an iOS device (e.g. iPhone) and has a native UI package. 
 Why not to try then? :)
 
 What I've done for now:
 - a UI with current server power state and either start, or stop buttons
 - a Wake-on-LAN code to start if the server appears to be down
 - a Shutdown section that powers my server off when it seems to be down
 
### Implementation:
Web server to serve our status and power actions:
- Install a web server (any really)
- upload two sample scripts from **web-scripts** dir
- allow sudo/selinux for the web user:

sudoers (add permission to shutdown the server):
```
Cmnd_Alias SHUTDOWN = /sbin/shutdown -P +0
odduser ALL = (root) NOPASSWD: SHUTDOWN
Defaults!SHUTDOWN !requiretty
```
- use `chcon` to grant execute permission to your scripts
- make sure you protect your scripts properly

Both scripts are written in Bash for simplification, feel free to modify for your needs

Pyhonista:
- Install Pythonista - [see this link](https://omz-software.com/pythonista/)
- Make sure to use iCloud, if you prefer to develop on a Mac or iPad and sync quickly between your devices
- I use Shortcuts from Apple ([link](https://apps.apple.com/us/app/shortcuts/id915249334)) to run my app quickly, just
get my shortcut from [this link](https://www.icloud.com/shortcuts/10147676d9cb42169c888a725594dd2f)
- Copy **server_mgmt.py** from **Pythonista 3** into the same location in your iCloud

You should see the following after you run the shortcut:

![status](https://vyakovlev.com/projects/srv-mgmt-pythonista/status1.png)

#### Let's configure **server_mgmt.py** script: please check inline comments and adjust to your needs.

### Some screenshots:

![screen shot1](https://vyakovlev.com/projects/srv-mgmt-pythonista/sc1.png)

![screen shot2](https://vyakovlev.com/projects/srv-mgmt-pythonista/sc2.png)

![screen shot3](https://vyakovlev.com/projects/srv-mgmt-pythonista/sc3.png)
