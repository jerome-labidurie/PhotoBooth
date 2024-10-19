#!/usr/bin/env python

# press/release quickly button for start/stop photobooth service
# hold button for >2s for shutdown


from gpiozero import Button
from subprocess import check_call, CalledProcessError, STDOUT
from signal import pause
import os

shutdown_btn = Button(3, hold_time=2)
FNULL = open(os.devnull, 'w')

def shutdown():
	#print ("btn held")
	check_call(['poweroff'])

def stop_start():
	#print ("btn released")
	try:
		check_call(['systemctl', 'status', 'photobooth.service'])
		# no error, service is running, stop it
		#print("Stopping photobooth")
		check_call(['systemctl', 'stop', 'photobooth.service'])
	except CalledProcessError:
		# error, service is not running, start it
		#print("Starting photobooth")
		check_call(['systemctl', 'restart', 'copy-overlays.service'])
		check_call(['systemctl', 'start', 'photobooth.service'])

# GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.wait_for_edge(3, GPIO.FALLING)

shutdown_btn.when_held = shutdown
shutdown_btn.when_released = stop_start

pause()
