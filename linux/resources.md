# Other resources

## Table of contents



# Linux VM in your own system





### Command to start the wsl 2 from windows

```
wsl --set-default-version 2
sudo apt-get update && sudo apt-get upgrade -y
sudo apt install xrdp -y
sudo service xrdp start
ip add
```


#### [Ubuntu Server for ARM](https://ubuntu.com/download/server/arm)
### Setup ubuntu server in UTM
```
sudo apt update && sudo apt upgrade -y
sudo apt install ubuntu-desktop
sudo reboot

# for directory sharing between host os and guest os (127.0.0.1:9843)
sudo apt install spice-vdagent spice-webdavd -y 

# https://docs.getutm.app/guest-support/linux/
sudo mkdir -p /media/shared
sudo mount -t 9p -o trans=virtio share /media/shared -oversion=9p2000.L
# You can also modify `sudo vi /etc/fstab` and add the following line to automatically mount the share on startup
share	/media/shared	9p	trans=virtio,version=9p2000.L,rw,_netdev,nofail	0	0
sudo chown -R $USER /media/shared

```




### Steps for creating my personalised VM in mac
- Create the VM from ubuntu image [[linux]]
- Add git ssh keys
- Add vm user name host in your ~/.ssh/config
- Setup ssh agent on vscode
	- [Linux VMs on an M1-based Mac with VScode and UTM](https://medium.com/@lizrice/linux-vms-on-an-m1-based-mac-with-vscode-and-utm-d73e7cb06133)
- Download and set zsh
- Install luajit then install neovim by luajit
