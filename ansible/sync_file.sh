#!/bin/bash
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# Skrip untuk menyalin isi direktori menggunakan rsync
rsync -av --delete /home/kpc/Network_Monitoring/output/ /mnt/c/Users/admin/Documents/
