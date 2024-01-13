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
        if len(args) > 1:
            print("** you can create at most one instance **")
        elif len(args) == 0:
            print("** class name missing **")
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
        if len(args) > 2:
            print("** you can only give class name and instance id **")
        elif len(args) == 0:
            print("** class name missing **")
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

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id.

        Usage: destroy <class_name> <instance_id>
        """
        args = line.split()
        if len(args) > 2:
            print("** you can only give class name and instance id **")
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in available_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = str(args[0]) + '.' + str(args[1])
            if not storage.del_obj(key):
                print("** no instance found **")

    def do_update(self, line):
        """
        Update an instance based on the class name and id.

        Usage: update <class_name> <instance_id> <attr_name> "<attr_value>"
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in available_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = str(args[0]) + '.' + str(args[1])
            obj = storage.get_obj(key)
            if obj is None:
                print("** no instance found **")
            else:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    curr_val = getattr(obj, args[2], None)
                    new_val = args[3]
                    if curr_val is not None:
                        if isinstance(curr_val, int):
                            new_val = int(new_val)
                        if isinstance(curr_val, float):
                            new_val = float(new_val)
                        if isinstance(curr_val, str):
                            new_val = str(new_val)
                    setattr(obj, args[2], new_val)
                    obj.save()

    def emptyline(self):
        """Do nothing."""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
