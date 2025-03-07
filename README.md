# **Network Switch Monitoring with Ansible and Jinja2**

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white) ![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## **Overview**

This project demonstrates the automation of network switch monitoring using **Ansible** and **Jinja2** templates. It was developed as part of my internship at **Kaltim Prima Coal (KPC)**, where I explored ways to streamline network operations and improve visibility into switch performance and status.

The solution automates the collection of critical network data (e.g., interface status, VLAN configurations, and device uptime) from managed switches and generates human-readable reports using Jinja2 templates. This approach reduces manual effort, minimizes errors, and provides consistent reporting for network administrators.

---

## **Features**

- **Automated Data Collection**: Uses Ansible playbooks to gather switch information via SNMP or CLI commands.
- **Dynamic Report Generation**: Leverages Jinja2 templates to create customizable and professional reports.
- **Scalable Architecture**: Designed to handle multiple switches and adapt to various network environments.
- **Extensible Framework**: Easily extendable to include additional monitoring metrics or support new devices.

---

## **Technologies Used**

- **Ansible**: For automating interactions with network devices.
- **Jinja2**: For generating dynamic and formatted reports.
- **SNMP/CLI**: Protocols used to retrieve data from network switches.
- **Python**: For scripting and integrating additional functionality if needed.
- **Markdown**: For documentation and reporting.

---

## **Project Structure**
├── ansible/
│ ├── ansible/ # Inventory files for network devices
│ │ └── inventory.yaml # List of managed switches
│ | └── network_monitoring.yaml # Ansible playbooks for monitoring tasks
│ │ └── configure_vlan.yaml # playbook for configuring vlan
│ | └── set_ip.yaml # playbook for set ip
│ | └── vault.yaml # secured place to store password
│ ├── templates/
│ │ └── index.yaml # Jinja2 template for index
│ | └── interface_report.yaml # Jinja2 template for interface report
│ | └── port_report.j2 # Jinja2 template for report generation
| | └── interfaces_data.j2 # Jinja2 template for interfaces data
│ | └── utilization_report.j2 # Jinja2 template for device report
| | └── vlan_report.j2 # Jinja2 report for vlan
| ├── switch_data # Folder for storing data


Acknowledgments
Special thanks to Kaltim Prima Coal (KPC) for providing the opportunity to work on this project during my internship.
Inspired by the power of automation tools like Ansible and Jinja2 to simplify network operations.
