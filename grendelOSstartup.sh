#this script starts needed software for parallel computing on grendel.
#the openAllcommand only starts the hardware.  
#alpha version 4 july 18 chrisrehm
echo ""
echo ""
echo "!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!"
echo "!*!*!*!*!*!*!             beginning grendel one softare  start up                     !*!*!*!*!*!*!"
echo "                      this takes several minutes. please be patient"
echo "       starting hardware start up routine, this takes approximately  5 minutes"
echo "                               Grendel says: "
echo "          Relax, and make yourself a nice cup of tea while you are waiting."
echo ""
echo "!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!"
echo ""

openAll    #uncomment if you want to use this to start hardware and software.

echo "!+!+!		System pause while computers bootload and start services "
sleep 1m
echo "!+!+!		Hardware setup should be complete "

echo "!*!*! !!!!! Would you like to upgrade all system software? [Y,n]"
read input
if [[ $input == "Y" || $input == "y" ]]; then        
        echo "!+!+!		Starting software setup "
        echo "!+!+!		Starting software upgrades on all computers"
        upgradeAll
        echo"!+!+!		Finished sofwar#ed upgrades"
else
        echo "!*!*!    Proceeding with boot routine. "
	sleep 1m
fi

#start NFS servers 

echo "!+!+!		Starting NFS servers "

#ssh pi@192.168.0.102 sudo startNFSserver
ssh pi@192.168.0.103 sudo startNFSserver
ssh pi@192.168.0.104 sudo startNFSserver

echo "!+!+!		Finished all NFS server starts "

sleep 10s

#start NFS clients on all computers

echo "!+!+!		Mounting NFS disks on all system computers "

ssh pi@192.168.0.101 mountAllDisks
ssh pi@192.168.0.102 mountAllDisks
ssh pi@192.168.0.103 mountAllDisks
ssh pi@192.168.0.104 mountAllDisks
ssh pi@192.168.0.105 mountAllDisks
ssh pi@192.168.0.106 mountAllDisks
mountAllDisks
echo "!*!*!		 All Drives mounted "
#start jupyter notebooks and ipyparallel ( not written yet)
echo "!+!+!		Starting Jupyter Notebooks and ipyparallel on all system computers "
echo "!§!§!          	This section is not yet implented "
echo "!+!+!		Finished starting Jupyter Notebooks and associated software "
echo ""
echo ""
echo "!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!"
echo "!*!*!*!*!*!          Hardware and software system setup is complete         !*!*!*!*!*!*!"
echo "!*!*!*!*!*!         The Grendel One Super Cluster for AGI Reseach is        !*!*!*!*!*!*!"
echo "!*!*!*!*!*!                          up and running.                        !*!*!*!*!*!*!"
echo "!*!*!*!*!*!                    Please enjoy your time here                  !*!*!*!*!*!*!"
echo "!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!"
echo ""
echo ""
