from proxmoxer import ProxmoxAPI
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("PROXMOX_HOST")
user = os.getenv("PROXMOX_USER")
token_name = os.getenv("PROXMOX_TOKEN_NAME")
token_value = os.getenv("PROXMOX_TOKEN_VALUE")
verify_ssl = os.getenv("PROXMOX_VERIFY_SSL", "False").lower() == "true"

proxmox = ProxmoxAPI(
    host,
    user,
    token_name,
    token_value,
    verify_ssl,
)
