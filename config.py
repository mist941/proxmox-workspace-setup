os_iso_dict = {
    "Ubuntu Server": "ubuntu-24.04.2-live-server-amd64.iso",
    "CentOS Stream": "CentOS-Stream-10-latest-x86_64-dvd1.iso",
    "Fedora Server": "Fedora-Server-netinst-x86_64-42-1.1.iso",
    "Debian": "debian-12.10.0-amd64-netinst.iso",
}

lxc_os_dict = {
    "Alpine": "alpine-3.21-default_20241217_amd64.tar.xz",
    "Arch": "archlinux-base_20240911-1_amd64.tar.zst",
    "Fedora": "fedora-42-default_20250428_amd64.tar.xz",
    "OpenSUSE": "opensuse-15.6-default_20240910_amd64.tar.xz",
}

os_dict = {
    "VM": list(os_iso_dict.keys()),
    "LXC": list(lxc_os_dict.keys()),
}
