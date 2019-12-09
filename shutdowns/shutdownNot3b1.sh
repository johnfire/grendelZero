#!/bin/bash
echo "Starting all but 3b1 shutdown now!"

USERNAME=pi
HOSTS="192.168.0.101 192.168.0.102 192.168.0.103 192.168.0.105"

SCRIPT="sudo systemctl stop nfs-kernel-server; sudo shutdown -H 1"

for HOSTNAME in ${HOSTS} ; do
    ssh ${USERNAME}@${HOSTNAME} "${SCRIPT}"
done


echo "All computers but 3b1 will be shut down in less than 1 minute."