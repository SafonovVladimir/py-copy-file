def copy_file(command_line: str) -> None:
    command, old_file, new_file = command_line.split()

    if command == "cp" and old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
            print(f"File {old_file} has been copied to the file {new_file}")
