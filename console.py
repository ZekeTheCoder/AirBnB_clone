#!/usr/bin/env python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB application with a custom prompt '(hbnb)'
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.

        Usage: Press (Ctrl+D)
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty input.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
