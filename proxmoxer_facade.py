from proxmoxer import ProxmoxAPI
import os
from dotenv import load_dotenv

load_dotenv()


class Proxmox:
    def __init__(self) -> None:
        try:
            self.__node = os.getenv("PROXMOX_NODE")
            self.__initialize()
        except Exception as e:
            print(e)

    def __initialize(self) -> None:
        """
        Initialize the Proxmox API.
        """
        try:
            proxmox = ProxmoxAPI(
                host=os.getenv("PROXMOX_HOST"),
                user=os.getenv("PROXMOX_USER"),
                password=os.getenv("PROXMOX_PASSWORD"),
                verify_ssl=False,
            )
            self.__proxmox = proxmox
        except Exception as e:
            print(f"Error initializing Proxmox: {e}")

    def get_next_vm_id(self) -> int:
        """
        Get the next available VM ID for the node.
        """
        try:
            qemu_vms = self.__proxmox.nodes(self.__node).qemu.get()
            lxc_cts = self.__proxmox.nodes(self.__node).lxc.get()
            qemu_ids = [vm["vmid"] for vm in qemu_vms]
            lxc_ids = [ct["vmid"] for ct in lxc_cts]
            all_ids = [int(id) for id in [*qemu_ids, *lxc_ids]]
            return max(all_ids) + 1 if all_ids else 100
        except Exception as e:
            print(f"Error getting next VM ID: {e}")
            return 100

    def create_vm(self, vmid: int, name: str, iso_src: str) -> None:
        try:
            self.__proxmox.nodes(self.__node).qemu.post(
                vmid=vmid,
                name=name,
                cores=1,
                memory=2048,
                net0="virtio,bridge=vmbr0",
                ide2=f"local:iso/{iso_src},media=cdrom",
                sata0="local-lvm:35",
                boot="order=ide2;net0",
                bootdisk="sata0",
                ostype="l26",
            )
        except Exception as e:
            print(f"Error creating VM: {e}")

    def start_vm(self, vmid: int) -> None:
        try:
            self.__proxmox.nodes(self.__node).qemu(vmid).start.post()
        except Exception as e:
            print(f"Error starting VM: {e}")

    def create_lxc(self, vmid: int, name: str, template: str) -> None:
        try:
            self.__proxmox.nodes(self.__node).lxc.post(
                vmid=vmid,
                hostname=name,
                ostemplate=template,
                storage="local-lvm",
                memory=512,
                cores=1,
                net0="name=eth0,bridge=vmbr0,ip=dhcp",
                rootfs="local-lvm:8",
            )
        except Exception as e:
            print(f"Error creating LXC: {e}")

    def start_lxc(self, vmid: int) -> None:
        try:
            self.__proxmox.nodes(self.__node).lxc(vmid).start.post()
        except Exception as e:
            print(f"Error starting LXC: {e}")
