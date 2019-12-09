!/bin/bash
echo "Starting 105 shutdown now!"

USERNAME=pi
HOSTS="192.168.0.105"

SCRIPT="sudo shutdown -H 1"

for HOSTNAME in ${HOSTS} ; do
    ssh ${USERNAME}@${HOSTNAME} "${SCRIPT}"
done


echo "105 will be shut down in less than 1 minutes."
