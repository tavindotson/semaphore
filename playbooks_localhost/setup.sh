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

ansible-playbook setup.yml --ask-become-pass
