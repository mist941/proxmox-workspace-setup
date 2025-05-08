from proxmoxer_facade import Proxmox
import questionary


def main():
    proxmox = Proxmox()
    vm_id = proxmox.get_next_vm_id()
    print(vm_id)
    choice = questionary.select(
        "Select the OS:",
        choices=[
            "🍃 Mint Cinnamon",
            "🍊 Ubuntu",
            "🥝 Debian",
        ],
    ).ask()
    print(choice)


if __name__ == "__main__":
    main()
