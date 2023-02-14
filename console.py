#!/usr/bin/python3
"""This is the main console for AirBnB"""

import cmd
from models.base_model import BaseModel
import models



class HBNBCommand(cmd.Cmd):
    """AirBnB console main class"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Handle End Of File"""
        return True

    def do_quit(self, arg):
        """Exit program"""
        return True

    def emptyline(self):
        """If line is empty don't do anything"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                cls = models.classes[arg]
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)

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
                        print(models.storage.all()[key])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name and id
         (save the change into the JSON file).
         Ex: $ destroy BaseModel 1234-1234-1234.
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
                        objects = models.storage.all()
                        models.storage.delete(objects[key])
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        if len(arg) == 0:
            print([str(value) for value in models.storage.all().values()])
        elif arg not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in models.storage.all().items()
                   if arg in key])

 

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class: <class name>.count()
        """
        if len(arg) == 0:
            print(len([str(value) for value in models.storage.all().values()]))
        elif arg in models.classes:
            print(len([str(value) for key, value in
                       models.storage.all().items()
                      if arg in key]))
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
