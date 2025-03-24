#!/bin/bash
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

cd /home/kpc/Network_Monitoring/ansible

# Jalankan playbook Ansible
ansible-playbook -i inventory.yaml network_monitoring.yaml
