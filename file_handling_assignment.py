"""Tasks:
File Creation:
Create a Python script (file_handling_assignment.py) that does the following:
Creates a new text file named "my_file.txt" in write mode ('w').
Write at least three lines of text to the file, including a mix of strings and numbers.
File Reading and Display:
Enhance your script to read the contents of "my_file.txt" and display them on the console.
File Appending:
Modify the script to open "my_file.txt" in append mode ('a').
Append three additional lines of text to the existing content.
Error Handling:
Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError)."""

def main():
     try:
          file = open("my_file.txt", "w")
          file.write("Hi, I'm John!\n2 + 3 = 5.\nI'm a mathematician and a coder!")
          file.close()

          file_2 = open("my_file.txt", "a")
          file_2.write("\nI'm also a poet!\nI like playing ping pong.\nI love swimming!")
          file_2.close()

          file_3 = open("my_file.txt", "r")
          content = file_3.read()
          file_3.close
          print(content)

     except FileNotFoundError:
          print("Error: File not found!!!")

     except PermissionError:
          print("Error: Permission denied!!!")

     except Exception as exc:
          print(f"Error occured: str{exc}")
     
     finally:
          if 'file' in locals():
               file.close()

if __name__ == "__main__":
     main()