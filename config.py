from proxmoxer import ProxmoxAPI
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("PROXMOX_HOST")
user = os.getenv("PROXMOX_USER")
password = os.getenv("PROXMOX_PASSWORD")
verify_ssl = os.getenv("PROXMOX_VERIFY_SSL", "False").lower() == "true"

proxmox = ProxmoxAPI(
    host,
    user=user,
    password=password,
    verify_ssl=verify_ssl,
)

for node in proxmox.nodes.get():
    for vm in proxmox.nodes(node["node"]).qemu.get():
        print(f"{vm['vmid']}. {vm['name']} => {vm['status']}")
