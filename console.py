#!/usr/bin/python3
"""This is the console for AirBnB"""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Air Bnb main console cmd class
    """
    prompt = "(hbnb) "
    class_list = BaseModel
    def do_quit(self, arg):
        """
        quits or exits console
        """
        return True

    def do_EOF(self, arg):
        """
        handles the end of file
        """
        return True

    def do_help(self, arg):
        """
        pops up help menu
        """
        return True

    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                new_class = HBNBCommand.class_list
            except KeyError:
                print("** class doesn't exist **")
            else:
                new_object = new_class()
                new_object.save()
                print(new_object.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(models.storage.all())
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        print(models.storage.all())





    def postloop(self):
        print

if __name__ == '__main__':
    HBNBCommand().cmdloop()