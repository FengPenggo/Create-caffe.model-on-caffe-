#!/usr/bin/env sh
#compute the mean image from myself training lmdb
#N.B. this is available in data/myselfmean

TOOLS=./build/tools
DATA=./data/myself
EXAMPLE=./mydemo/dataset

$TOOLS/compute_image_mean.bin $EXAMPLE/myself_train_lmdb $EXAMPLE/mydata_mean.binaryproto
 
echo "Done!"
