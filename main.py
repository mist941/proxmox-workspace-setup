from proxmoxer_facade import Proxmox
import questionary
from config import os_iso_dict


def select_os():
    return questionary.select(
        "Select the OS:",
        choices=["Ubuntu Server", "CentOS Stream", "Fedora Server", "Debian"],
    ).ask()


def select_os_iso(os):
    return os_iso_dict[os]


def main():
    proxmox = Proxmox()
    vm_id = proxmox.get_next_vm_id()
    os = select_os()
    iso_src = select_os_iso(os)
    proxmox.create_vm(vmid=vm_id, name="VM", iso_src=iso_src)


if __name__ == "__main__":
    main()
