#! /bin/bash
cd rcrs-server/Scripts
pwd
. functions.sh

processArgs $*


# To create different log directories
echo $LOGDIR
#LOGDIR="$LOGDIR-$HOSTNAME"
LOGDIR="$LOGDIR-$HOSTNAME-$(date +"%T")"
#echo $LOGDIR
#mkdir $LOGDIR

# Delete old logs
rm -f $LOGDIR/*.log

#startGIS
startKernel --nomenu --autorun 
startSims


rm -f $LOGDIR/*.log

echo "Start your agents"
waitFor $LOGDIR/kernel.log "Kernel has shut down" 30

kill $PIDS
