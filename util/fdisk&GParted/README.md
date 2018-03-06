##### How to enlarge your disk of Linux in Vmware

1. Download and connect the iso of GParted.
2. Use GParted.(If swap-disk block the allocation of free space, delete and recreate it.)
3. Change /etc/fstab
4. Disk id : lsblk -f 

Don't forget to save the snapshot.