#!/bin/bash
echo "Starting 101  shutdown now!"

USERNAME=pi
HOSTS="192.168.0.101"

SCRIPT="sudo shutdown -H 1"

for HOSTNAME in ${HOSTS} ; do
    ssh ${USERNAME}@${HOSTNAME} "${SCRIPT}"
done


echo "A101 will be shut down in less than 1 minutes."
