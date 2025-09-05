# 🖋️ File Modifier with Error Handling

This Python script reads a user-specified text file, modifies each line by adding a prefix, and writes the updated content to a new file.

## 🚀 How It Works

1. Asks the user for a filename  
2. Adds the prefix `[MODIFIED]` to every line  
3. Writes the modified content to a new file named `modified_<original>.txt`  
4. Handles errors like missing files, permission issues, and unexpected exceptions

## 🧪 Example

**Input file**: `example.txt`

Hello world  
Python is awesome

**Output file**: `modified_example.txt`

[MODIFIED] Hello world  
[MODIFIED] Python is awesome

## ⚠️ Error Handling

- `FileNotFoundError` — File doesn't exist  
- `PermissionError` — You don't have permission to access the file  
- General `Exception` — Any unexpected runtime issues

## 📁 Files

- `file_modifier.py` — Main script  
- `README.md` — Project documentation  
- `LICENSE` — MIT License  

## 🧑‍💻 Author

Augusto Mate  
📧 mate.augusto.mz@gmail.com

## 🪪 License

This project is licensed under the [MIT License](./LICENSE).
