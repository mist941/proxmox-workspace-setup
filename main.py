from api import ProxmoxAPI
from dotenv import load_dotenv
import os


load_dotenv()


def main():
    proxmox = ProxmoxAPI(
        host=os.getenv("PROXMOX_HOST"),
        user=os.getenv("PROXMOX_USER"),
        password=os.getenv("PROXMOX_PASSWORD"),
        verify_ssl=False,
    )

    if proxmox.connect():
        print("Successfully authenticated!")
        print(f"Ticket: {proxmox.ticket}")
        print(f"CSRF Token: {proxmox.csrf_token}")
    else:
        print("Authentication failed!")


if __name__ == "__main__":
    main()
