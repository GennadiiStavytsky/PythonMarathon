from helper import print_stderr, print_stdout
import webbrowser
import re
import sys

if len(sys.argv) == 1:
    print_stderr("The site URL was not passed")

if not re.match("^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$", sys.argv[1]):
        print_stderr("The URL is invalid")

webbrowser.open(sys.argv[1])
print_stdout(f"Opening the YouTube video at {sys.argv[1]}")
print_stdout("YouTube video opened")