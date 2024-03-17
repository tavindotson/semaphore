import os

def list_yaml_files(folder):
    yaml_files = []
    for file in os.listdir(folder):
        if file.endswith(".yml"):
            yaml_files.append(file)
    return yaml_files

def select_playbook(yaml_files):
    print("Available playbooks:")
    for idx, playbook in enumerate(yaml_files):
        print(f"{idx+1}. {playbook}")
    selection = int(input("Enter the number of the playbook to run: "))
    if selection < 1 or selection > len(yaml_files):
        print("Invalid selection. Please choose a number from the list.")
        return select_playbook(yaml_files)
    else:
        return yaml_files[selection-1]

def run_playbook(playbook):
    os.system(f"ansible-playbook -i hosts.yml \"{playbook}\"")

if __name__ == "__main__":
    playbook_folder = "playbooks"
    yaml_files = list_yaml_files(playbook_folder)
    if not yaml_files:
        print("No YAML files found in the playbook folder.")
    else:
        selected_playbook = select_playbook(yaml_files)
        run_playbook(os.path.join(playbook_folder, selected_playbook))
