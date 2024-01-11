#!/usr/bin/python3
"""This is a module for the console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """A class for command interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, _line):
        """
        Exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, _line):
        """
        Exit the program.

        end-of-file marker
        Usage: Ctrl-D
        """
        return True

    def emptyline(self):
        """Do nothing."""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
