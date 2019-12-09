#!/bin/bash
echo "Starting system wide shutdown now!"

USERNAME=pi
HOSTS="192.168.0.101 192.168.0.102 192.168.0.103 192.168.0.104 192.168.0.105"

SCRIPT="sudo systemctl stop nfs-kernel-server.service; sudo shutdown -H 1"

for HOSTNAME in ${HOSTS} ; do
    echo "I am trying to shut down computer " ${HOSTNAME}
    ssh ${USERNAME}@${HOSTNAME} "${SCRIPT}"
done


echo "All computers will be shut down in less than 1 minute!."