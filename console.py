#!/usr/bin/env python3
""" Command Line Interface for HBNB application """


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB application with a custom prompt '(hbnb)'
    """

    prompt = '(hbnb) '
    classes = {"BaseModel"}

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

# Console 0.1
    def do_create(self, type_model):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id."""

        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            dictionary = {'BaseModel': BaseModel}
            my_model = dictionary[type_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name and id """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            for key, value in all_objects.items():
                object_name = value.__class__.__name__
                object_id = value.id
                if object_name == args[0] and object_id == args[1]:
                    print(value)
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
