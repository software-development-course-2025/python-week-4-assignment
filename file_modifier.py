def read_and_modify_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.readlines()

        # Modification: add a "[MODIFIED] " prefix to each line
        modified_content = [f"[MODIFIED] {line}" for line in content]

        new_filename = f"modified_{filename}"

        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)

        print(f"✅ File modified successfully! New file created: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("❌ Error: You don't have permission to read/write this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Main program
filename = input("📎 Enter the name of the file to read: ")
read_and_modify_file(filename)
