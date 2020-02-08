#!/bin/bash
echo "Starting 102 shutdown now!"

USERNAME=pi
HOSTS="192.168.0.102"

SCRIPT="sudo systemctl stop nfs-kernel-server.service;sudo shutdown -H 1"

ssh pi@192.168.0.102 ${SCRIPT}

for HOSTNAME in ${HOSTS} ; do
    ssh  ${USERNAME}@${HOSTNAME} "${SCRIPT}"
done


echo "102 will be shut down in less than 1 minutes."