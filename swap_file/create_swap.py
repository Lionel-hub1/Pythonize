#!/usr/bin/env python3
# This is the file to download and run on the server/computer runing unix/linux to create a swap file
import argparse
import os

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Create and configure swap file')
parser.add_argument('-s', '--size', help='Specify the swap file size in GB', type=float, required=True)
args = parser.parse_args()

swap_size = args.size

# Change to the root directory
os.chdir("/")

# Create a swap file named swapfile with the specified size
swap_file_path = "swapfile"
os.system(f"sudo fallocate -l {swap_size}G {swap_file_path}")
print(f"Created a {swap_size}GB swap file named {swap_file_path}")

# Set the permissions of the swapfile to 600 (rw-------)
os.system(f"sudo chmod 600 {swap_file_path}")
print("Set the permissions of the swapfile to 600 (rw-------)")

# Create a swap partition on the swapfile
os.system(f"sudo mkswap {swap_file_path}")
print(f"Created a swap partition on the {swap_file_path}")

# Enable the swap partition
os.system(f"sudo swapon {swap_file_path}")
print(f"Enabled the swap partition")

# Add the swapfile to the /etc/fstab file to make it persistent
os.system(f"sudo echo '/swapfile none swap sw 0 0' >> /etc/fstab")
print("Added the swapfile to the /etc/fstab file to make it persistent")

# Display the swap status
os.system("sudo swapon --show")
print("Displayed the swap status")
