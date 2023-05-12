#!/usr/bin/python3
"""Module containing the entry point of the command interpreter."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""
    prompt = '(hbnb) '
    class_names = ["BaseModel", "User"]

    def do_EOF(self, line):
        """Handle EOF signal."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, save it, and print id."""
        if not line:
            print("** class name missing **")
            return
        try:
            cls = eval(line)
            if not issubclass(cls, BaseModel):
                print("** class doesn't inherit from BaseModel **")
                return
        except NameError:
            print("** class doesn't exist **")
            return
        obj = cls()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """Show an instance's string representation by id."""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2

