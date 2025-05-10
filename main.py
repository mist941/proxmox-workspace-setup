from datetime import datetime
from proxmoxer_facade import Proxmox
import questionary
from config import os_iso_dict, lxc_os_dict


def select_type():
    return questionary.select(
        "Select the type:",
        choices=["VM", "LXC"],
    ).ask()


def select_os(type: str):
    return questionary.select(
        f"Select the {type} OS:",
        choices=["Ubuntu Server", "CentOS Stream", "Fedora Server", "Debian"],
    ).ask()


def get_vm_name(type: str):
    return questionary.text(
        f"Enter the {type} name:",
        default=f"{type}-{datetime.now().strftime('%Y%m%d%H%M%S')}",
    ).ask()


def get_os_iso(os):
    return os_iso_dict[os]


def get_lxc_template(os: str):
    return lxc_os_dict[os]


def create_vm(proxmox: Proxmox, vm_id: int, vm_name: str, iso_src: str):
    vm_id = proxmox.get_next_vm_id()
    os = select_os(type="VM")
    vm_name = get_vm_name(type="VM")
    iso_src = get_os_iso(os)
    proxmox.create_vm(vmid=vm_id, name=vm_name, iso_src=iso_src)
    proxmox.start_vm(vmid=vm_id)


def create_lxc(proxmox: Proxmox):
    vmid = proxmox.get_next_lxc_id()
    lxc_name = get_vm_name(type="LXC")
    os = select_os(type="LXC")
    template = get_lxc_template(os)
    proxmox.create_lxc(vmid=vmid, name=lxc_name, template=template)
    proxmox.start_lxc(vmid=vmid)


def main():
    proxmox = Proxmox()
    type = select_type()
    if type == "VM":
        create_vm(proxmox)
    elif type == "LXC":
        create_lxc(proxmox)


if __name__ == "__main__":
    main()
