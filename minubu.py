import sys
import platform
import argparse

import colorama
import psutil
import termcolor

colorama.init()


# if ubuntu
def is_ubu():
    try:
        with open("/etc/os-release", "r") as file:
            os_release = file.read().lower()

        return "id=ubu" in os_release or "id_like=" in os_release and "ubuntu" in os_release

    except (FileNotFoundError, PermissionError):
        return False


# --issue
parser = argparse.ArgumentParser(
    description=termcolor.colored(
        "minubu - a system information tool for ubuntu.",
        "cyan",
        "on_black"
    )
)

parser.add_argument(
    "--issue",
    action="store_true",
    help=termcolor.colored(
        "if you have an issue with the tool, contact me on discord "
        "@ak0101101 or on github: https://github.com/akx25/minubu/issues",
        "yellow"
    )
)

args = parser.parse_args()


if args.issue:
    print(
        termcolor.colored(
            "if you have an issue with minubu, contact me on discord or gitHub:",
            "yellow"
        )
    )
    print(termcolor.colored("discord: @ak0101101", "magenta"))
    print(
        termcolor.colored(
            "github: https://github.com/akx25/minubu/issues",
            "black",
            "on_white"
        )
    )
    sys.exit(0)


#host
def get_host():
    return platform.node()


#os
def get_os():
    if not is_ubu():
        return termcolor.colored("your os is not ubuntu!", "yellow")

    try:
        with open("/etc/os-release", "r") as file:
            for line in file:
                if line.startswith("PRETTY_NAME="):
                    return line.strip().split("=", 1)[1].strip('"')

    except (FileNotFoundError, PermissionError):
        pass

    return "ubuntu"


# memory
def get_memory():
    memory = psutil.virtual_memory()
    return f"{memory.total / (1024 ** 3):.2f} gb"


# disk usage
def get_disk():
    disk = psutil.disk_usage("/")
    return f"{disk.total / (1024 ** 3):.2f} gb"


# logo
logo = [
    termcolor.colored(r"  _   _ _             _        ", "red"),
    termcolor.colored(r" | | | | |__ _  _ _ _| |_ _  _ ", "red"),
    termcolor.colored(r" | |_| | '_ \ || | ' \  _| || |", "red"),
    termcolor.colored(r"  \___/|_.__/\_,_|_||_\__|\_,_|", "red"),
]


info = [
    f"host:   {get_host()}",
    f"os:     {get_os()}",
    f"memory: {get_memory()}",
    f"disk:   {get_disk()}",
]


#logo place
#logo place
for i in range(max(len(logo), len(info))):
    left = logo[i] if i < len(logo) else ""
    right = info[i] if i < len(info) else ""

    spaces = 20 - len(left) + (len(left) - len(left.replace("\x1b", "")))

    print(f"{left}{' ' * max(1, spaces)}{right}")
