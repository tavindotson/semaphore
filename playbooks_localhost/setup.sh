#!/usr/bin/env bash

echo "Create a user first, then run this as the user you want to setup."

sleep 3

read -p "Are you sure you want to continue? [y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Continuing..."
else
    echo "Exiting..."
    exit 1
fi

sudo apt update
sudo apt install ansible -y
ansible-playbook setup.yml --ask-become-pass
echo "Done"
echo
echo "Do the following manually:"
echo "  - Start UFW"
echo "  - Edit .zshrc to include plugins"
echo "  - Add .hushlogin file"
echo "  - Remove /etc/motd"
