# semaphore

## Warning

This repo is not optimized for anyone to use; I hardcoded some SSH public keys and user names. I will update it in the future to be more usable. It will change dramatically over time.

`./playbooks_localhost` folder should for for anyone.

You can start the `.run.py` file directly, the start script will evolve to do checks
before running the playbooks.

## Requirements

- Debian or Ubuntu based Linux
- Ansible

## If you want to setup or get info from remote hosts

1. Clone this repo and enter into it
1. Edit the hosts.yml file as needed `nano hosts.yml`
1. `./start`

## If you want to setup your local device

1. Clone this repo and enter into it
1. `cd playbooks_localhost`
1. `./setup.sh`
