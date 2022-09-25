#!/bin/bash
# copy overlays if presents on the USB key

if [ -r /home/pi/Pictures/overlays/1.png ]
then
   echo "copy overlays ..."
   cp /home/pi/Pictures/overlays/*.png /home/pi/photobooth/
   chown pi:pi /home/pi/photobooth/*.png # make sure owned by pi
fi

