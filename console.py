#!/usr/bin/python3
"""Documenting all the modules"""

import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
"""Importing the cmd inbuilt module"""


class HBNBCommand(cmd.Cmd):
    """
    class that contains the entry point of
    the command interpreter:
    """
    prompt = "(hbnb) "

    def precmd(self, arg):
        """Responsible for the non-interactive mode"""
        if not sys.stdin.isatty():
            print()
        return arg

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        try:
            instance = globals()[class_name]()
            instance.save()
            print(instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Function responsible to show objects in the file"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        id_instance = args[1]
        key = "{}.{}".format(class_name, id_instance)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Responsible for deleting objects"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        id_instance = args[1]
        key = f"{class_name}.{id_instance}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Responsible for printing out objects to the console"""
        args = shlex.split(arg)
        if not args:
            print([str(obj) for obj in storage.all().values()])
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        class_instances = [
            str(obj) for key, obj in storage.all().items()
            if key.startswith(class_name + ".")
            ]
        print(class_instances)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id
        by adding or updating attribute
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in globals():
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = f'{args[0]}.{args[1]}'
            all_objs = storage.all()
            if key not in all_objs:
                print('** no instance found **')
            elif len(args) == 2:
                print('** attribute name missing **')
            elif len(args) == 3:
                print('** value missing **')
            else:
                obj = all_objs[key]
                attr_name = args[2]
                attr_type = type(getattr(obj, attr_name, ''))
                attr_value = attr_type(args[3].strip('"'))
                setattr(obj, attr_name, attr_value)
                obj.save()

    def emptyline(self):
        """
        Overrides the empty line function to change
        default behaviour
        """
        pass

    def do_quit(self, arg):
        """Help to quit interpreter"""
        return True

    def do_EOF(self, arg):
        """End of file """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
