#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
"""Importing the cmd inbuilt module"""

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    """
    class that contains the entry point of
    the command interpreter:
    """
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        
        class_name =arg.split()[0]
        try:
            instance = globals()[class_name]()
            instance.save()
            print(instance.id)
        except KeyError:
            print("** class doesn't exist **")

   #Work in progess 
    # def do_show(self, arg):
    #     """
    #     Prints the string representation of an instance
    #     based on the class name and id.
    #     """
    #     get_argument = arg.split()
    #     if not get_argument:
    #         print("** class name missing **")
    #         return
        
    #     class_name = get_argument[0] 
    #     id_class = get_argument[1]
        
    #     if not id_class:
    #         print("** instance id missing **")
    #         return
        
    #     if class_name not in globals()[class_name]():
    #         print("** class doesn't exist **")

    #     key = f"{class_name}.{id_class}"
    #     if key in storage.all():
    #         print(storage.all()[key])
        
        
        

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
