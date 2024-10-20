## Software
* camera_btn.py : PhotoBooth main daemon. handle taking picture and upload to google drive
* listen-for-shutdown.py : management software :
  * starting/stopping camera_btn.py (short press)
  * powering off RPi (long press)
* *.service : systemctl services definition

## Install

Based on [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)

Install shutdown service

    sudo cp listen-for-shutdown.service /etc/systemd/system/
    sudo systemctl daemon-reload
    sudo systemctl enable listen-for-shutdown.service
    sudo systemctl start listen-for-shutdown.service

Install Photobooth service

    sudo cp photobooth.service /etc/systemd/system/
    sudo systemctl daemon-reload
    sudo systemctl enable photobooth.service
    sudo systemctl start photobooth.service

Install Overlays service (to copy overlays from usb key during startup)

    sudo cp copy-overlays.service /etc/systemd/system/
    sudo systemctl daemon-reload
    sudo systemctl enable copy-overlays.service

Link data dir to USB key (when plugged)

    cd /home/pi
    ln -s /media/pi/DISK_IMG/ Pictures
    mkdir Pictures/overlays

**Warning:** when multiple usb keys are used, the mounting directory (in `/media/pi/`) can change. In this case, the link has to be recreated/updated.

Symptoms are: the application crash while taking the photo (no *Merci* screen) and no pictures are created on the usb key.

add to /boot/config.txt

    # enable uart for "power" led
    enable_uart=1

Install needed python modules

    pip install --upgrade google-api-python-client

get api ID clients OAuth 2.0 client_id.json and put in current directory. See https://console.developers.google.com/apis/credentials

## Customization
There's some images displayed by the PhotoBooth service. They are overlayed on top of the live image.
* Acceuil.png : displayed all when waiting for a "customer"
* 3.png / 2.png / 1.png : countdown before picture shooting
* Merci.png : displayed after shooting, before showing taken picture

There's a svg template for creating the overlays
* modify the layers
* export each layer to a png (2568x1926)
