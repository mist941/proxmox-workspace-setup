from proxmoxer_facade import Proxmox


def main():
    proxmox = Proxmox()
    print(proxmox.get_next_vm_id())


if __name__ == "__main__":
    main()
