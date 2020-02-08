#!/bin/bash
echo "Starting 103 shutdown now!"

USERNAME=pi
HOSTS="192.168.0.103"

SCRIPT="sudo systemctl stop nfs-kernel-server.service; shutdown -H 1"

for HOSTNAME in ${HOSTS} ; do
    ssh ${USERNAME}@${HOSTNAME} "${SCRIPT}"
done


echo "103 will be shut down in less than 1 minutes."