#!/bin/bash
#mount all grendel drive script for a given computer.

echo "starting NFS folders mounting proceedures on 110"

echo "mounting GrendelDrive on 110"
sudo mount 192.168.0.102:/media/pi/GrendelDrive /media/grendelData102
echo "mounted GrendelDrive on 110"

echo "mounting linuxsystem on 110"
sudo mount 192.168.0.103:/media/pi/linuxsystem /media/grendelData103
echo "mounted linuxsystem on 110"

echo "mounting OldDataLenovo on 110"
sudo mount 192.168.0.103:/media/pi/OldDataLenovo /media/grendelData104
echo "mounted OldDataLenovo on 110"

echo "mounted all disks on 110"


