#!/usr/bin/python3
"""This is a module for the console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


available_classes = ['BaseModel', 'User',
                     'State', 'City', 'Place', 'Amenity', 'Review']


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

    def do_create(self, line):
        """
        Create a new instance of a class.

        Usage: create <class_name>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) > 1:
            print("** you can create at most one instance **")
        else:
            args = args[0]
            new_obj = None
            if args == 'BaseModel':
                new_obj = BaseModel()
            elif args == 'User':
                new_obj = User()
            elif args == 'State':
                new_obj = State()
            elif args == 'City':
                new_obj = City()
            elif args == 'Place':
                new_obj = Place()
            elif args == 'Amenity':
                new_obj = Amenity()
            elif args == 'Review':
                new_obj = Review()
            else:
                print("** class doesn't exist **")
            if new_obj:
                print(new_obj.id)
                new_obj.save()

    def do_show(self, line):
        """
        Print the string representation of an instance.

        Usage: show <class_name> <instance_id>
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) > 2:
            print("** you can only give class name and instance id **")
        elif args[0] not in available_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = str(args[0]) + '.' + str(args[1])
            obj = storage.get_obj(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print all string representation of all instances.

        Usage: all [<class_name>]
        """
        args = line.split()
        if len(args) > 1:
            print("** you can write one or zero classes **")
        else:
            ans = []
            objects = storage.all()
            if len(args) == 0:
                for obj in objects.values():
                    ans.append(str(obj))
            else:
                if args[0] not in available_classes:
                    print("** class doesn't exist **")
                    ans = None
                else:
                    for obj in objects.values():
                        if obj.__class__.__name__ == args[0]:
                            ans.append(str(obj))
            if ans is not None:
                print(ans)

    def emptyline(self):
        """Do nothing."""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
