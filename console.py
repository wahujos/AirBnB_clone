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
        """Responsible for updating attributes in the objects"""
        args = shlex.split(arg)
        if len(args) == 0:
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
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        value_str = args[3]
        instance = storage.all()[key]

        if not hasattr(instance, attribute_name):
            setattr(instance, attribute_name, value_str)
            instance.save()
            return

        attribute_type = type(getattr(instance, attribute_name, None))
        try:
            # if attribute_type is not None:
            #     if attribute_type is not type(None):
            #         value = attribute_type(value_str)
            #     else:
            #         value = value_str
            # else:
            #     value = value_str

            # if attribute_type is not None and
            # attribute_type is not type(None):
            # if attribute_type is not None and\
            #     not isinstance(attribute_type, None):
            if attribute_type and not isinstance(attribute_type, type(None)):
                value = attribute_type(value_str)
        except ValueError:
            print("** invalid value **")
            return
        setattr(instance, attribute_name, value)
        instance.save()

    def default(self, line):
        """The default function"""
        parts = line.split('.')
        if parts[0] in globals():
            if parts[1] == 'all()':
                self.do_all(parts[0])
            elif parts[1] == 'count()':
                lin = [
                        v for k, v in storage.all().items()
                        if k.startswith(parts[0])
                        ]
                print(len(lin))
                return
            elif parts[1].startswith('show'):
                p1 = parts[1].split('(')
                p2 = p1[1].split('"')
                self.do_show("{} {}".format(parts[0], p2[1]))
            elif parts[1].startswith('destroy'):
                p1 = parts[1].split('(')
                p2 = p1[1].split('"')
                self.do_destroy("{} {}".format(parts[0], p2[1]))

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
