# semaphore

## Warning

This repo is not optimized for anyone to use; I hardcoded some SSH public keys and user names. I will update it in the future to be more usable.

`./playbooks_localhost` folder should for for anyone.

## Requirements

- Debian or Ubuntu based Linux
- Ansible

## If you want to setup or get info from remote hosts

1. Clone this repo and enter into it
1. Edit the hosts.yml file as needed `nano hosts.yml`
1. `chmod u+x start`
1. `./start`

## If you want to setup your local device

1. Clone this repo and enter into it
1. `cd playbooks_localhost`
1. `chmod u+x setup.sh`
1. `./setup.sh`
