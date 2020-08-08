#!/usr/bin/python

import os
import os.path

VOLEXEC = 'python ~/Desktop/pyvol/volatility/vol.py '
PYVOLDIR='./'
OPTIONS = ["-h", "-f", "-d", "--profile", "-w", "--output", "--output-file", "-v"]

class Pyvol:

    def __init__(self, file = None, options = [], command = None, outputfile = None):
        self.options = []
        self.file = file
        self.command = command
        self.outputfile = outputfile
        self.tabs = []

    def add_file(self, file):
        if not os.path.exists(file):
            print("File not found")
            return
        elif self.file != None:
            print(str(self.file) + " is already loaded")
            return
        else:
            self.file = file
            file_option = "-f " + str(file)
            self.add_option(file_option)
            print("File found and loaded")

    def remove_file(self):
        if self.file == None:
            print("No file is present")
        else:
            self.file = None
            print("File removed")

        return self.file == None

    def add_option(self, option):
        if option == None or option == "":
            print("No options listed")
            return
        else:
            opt_arr = option.split(" ")

            if len(opt_arr) == 1 and str(opt_arr[0]) == "-h":
                self.options.append(opt_arr)
                print("Option added")
                return

            if len(opt_arr) != 2:
                print("Invalid number of options listed")
                return
            if str(opt_arr[0]) not in OPTIONS:
                print("Invalid option flag listed")
                return

            self.options.append(opt_arr)
            print("Option added")
            return

    def remove_option(self, option):
        pass

    def format_options(self):
        if len(self.options) == 0:
            return None

        formatted_options = ""
        for option in self.options:
            for param in option:
                formatted_options = formatted_options + " " +  str(param)

        if self.command != None:
            formatted_options = formatted_options + " " + str(self.command)

        return str(formatted_options)

    def add_command(self, command):
        # TODO - Check if valid command
        if command != None and command != "":
            self.command = command
            print("Command added")
            return
        else:
            print("Command not added")
            return

    def remove_command(self):
        if self.file == None:
            print("No file is present")
            return
        else:
            self.file = None
            print("File removed")
            return

    def add_outputfile(self, outputfile):
        if not os.path.exists(PYVOLDIR + str(outputfile)):
            file = open(PYVOLDIR + str(outputfile), 'a')
            file.write("")
            file.close()
        else:
            file = open(PYVOLDIR + str(outputfile), 'w')
            file.close()

        self.outputfile = str(outputfile)

    def execute(self):
        try:
            full_command = self.format_options()
            if full_command != None:
                # if self.outputfile != None:
                #     os.system( str(VOLEXEC) + str(full_command) + " > tmp/output/" + str(self.command) + "_output")
                # else:
                os.system( str(VOLEXEC) + str(full_command) + " > tmp/outputs/" + str(self.command) + "_output")

                # Make note of the command just executed by adding it to tabs
                self.tabs.append(self.command)

                # Reset inpreparation for the next execution request
                self.file = None
                self.command = None
                self.options = []
                self.outputfile = None

        except Exception as e:
            print(e)

    def getTabs(self):
        return self.tabs

    def filter(self, file, filter):
        print(file)
        print(filter)

        base_file = "tmp/outputs/" + file

        if not os.path.exists(base_file):
            return False
        if filter == None or filter == "":
            return False

        filter_file = f"tmp/filters/{file}"
        os.system("grep " + str(filter) + " " + base_file + " > " + str(filter_file))

        if not os.path.exists(filter_file):
            return False

        return True



    def debug(self, extra = None):
        print("File: " + str(self.file))
        print("Options: " + str(self.options))
        print("Command: " + str(self.command))
        print("OutputFile: " + str(self.outputfile))
        if extra != None:
            print("Extra: " + str(extra))

if __name__ == "__main__":

    # Instantiate Pyvol
    pyvol = Pyvol()

    # Specify the output file
    pyvol.add_outputfile("out")

    # Give Pyvol the file you wish to examine
    pyvol.add_file("../mem_dumps/windows/sample001.bin")

    # Add an option to pyvol
    # pyvol.add_option("--profile WinXPSP2x86")

    # Add an option to pyvol
    # pyvol.add_option("--output-file test.out")

    # Add a command to execute on the file
    pyvol.add_command("imageinfo")

    # Execute the command
    pyvol.execute()

    pyvol.debug()

    exit()
