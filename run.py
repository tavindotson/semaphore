import os

def list_yaml_files(folder):
    """Returns a list of .yml files in the specified folder."""
    return [file for file in os.listdir(folder) if file.endswith(".yml")]

def select_playbook(yaml_files):
    """Displays a numbered list of available playbooks and returns the selected one."""
    print("\nAvailable Playbooks:")
    print("-" * 30)  # separator line
    for idx, playbook in enumerate(yaml_files, start=1):
        print(f"{idx}. {playbook}")
    print("-" * 30)  # separator line

    while True:
        try:
            selection = int(input("\nEnter the number of the playbook to run: "))
            if 1 <= selection <= len(yaml_files):
                return yaml_files[selection - 1]
            else:
                print("Invalid selection. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def run_playbook(playbook):
    """Runs the selected playbook using ansible-playbook."""
    os.system(f'ansible-playbook -i hosts.yml "{playbook}"')

def main():
    playbook_folder = "playbooks"
    yaml_files = list_yaml_files(playbook_folder)

    if not yaml_files:
        print("No YAML files found in the playbook folder.")
        return

    # Sort the yaml files alphabetically
    yaml_files.sort()
    selected_playbook = select_playbook(yaml_files)
    run_playbook(os.path.join(playbook_folder, selected_playbook))

if __name__ == "__main__":
    main()
