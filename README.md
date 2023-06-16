## Deliverable

Documentation, scripts on GitHub : https://github.com/CPNV-DGS-VIRT2/VIRT2

Wiki : https://github.com/CPNV-DGS-VIRT2/VIRT2/wiki

### Github

Here's how the GitHub is organized

```
.\README.md - This document
.\README-Complete.md - README + Wiki on the same MD File

.\wrapper-virt2.py - Wrapper script to execute in the proxmox VM

.\ansible\ - Contains the playbooks and inventory files for each container

.\ansible\kali
	.\Execution-Kali.md - Command used to run the playbook
	.\kali.cfg - Inventory file for Kali container
	.\playbook-kali.yaml - Playbook for Kali container

.\ansible\pentester
	.\Execution-Pentester.md - Command used to run the playbook
	.\pentest.cfg - Inventory file for Pentester container
	.\playbook-pentest.yaml - Playbook for Pentester container

.\assets\ - Images of this documentation, automaticaly created by the Typora app
```

