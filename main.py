from proxmoxer_facade import Proxmox
import questionary


def select_os():
    return questionary.select(
        "Select the OS:",
        choices=[
            "🍃 Mint Cinnamon",
            "🍊 Ubuntu",
            "🥝 Debian",
        ],
    ).ask()


def main():
    proxmox = Proxmox()
    vm_id = proxmox.get_next_vm_id()
    os = select_os()
    print(os)


if __name__ == "__main__":
    main()
