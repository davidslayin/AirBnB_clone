#!/usr/bin/python3

"""
Module console

Contain class Console
"""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """A siple command interpreter

    Attributes
    ----------
    prompt : str
        A prompt text

    methods
    -------
    do_quit(line)
        Quit command to exit the program
    do_EOF(line)
        Exit on Ctrl-D
    emptyline()
        Overwrite default behavior to repeat last cmd
    do_create(line)
        create a new object
    do_show(line)
        Prints the string representation of an instance
    do_destroy(line)
        Deletes an instance based on the class name and id
    do_all(line)
        Prints all string representation of all instances
        based or not on the class name
    do_update(line)
        Updates an instance based on the class name and id by adding
        or updating attribute
    dfault(line)
        Accepts class name followed by arguement
    parse(line)
        parse user typed input and change tuple
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        print("")
        return True

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_create(slef, line):
        """Creates an instance of class"""
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
        else:
            instance = storage.class_dict[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = parse(line)
        if line == "" or line is None:
            print("** class name missing **")
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = parse(line)
        if line == "" or line is None:
            print("** class name missing **")
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        if line != "":
            args = parse(line)
            if args[0] not in storage.class_dict:
                print("** class doesn't exist **")
            else:
                list_obj = [str(val) for ke, val in storage.all().items()
                            if val.__class__.__name__ == args[0]]
                print(list_obj)
        else:
            list_obj = [str(val) for key, val in storage.all().items()]
            print(list_obj)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute
        """
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[-1]))
            attr_update = args[-1]
            attr_update = attr_update.strip("'")
            attr_update = attr_update.strip('"')
            new_str = args[2:-1]
            attr_name = ""
            for i in range(len(new_str)):
                if i != len(new_str) - 1:
                    attr_name += new_str[i] + " "
                else:
                    attr_name += new_str[i]
                attr_name = attr_name.replace('"', "")
            setattr(storage.all()[key], attr_name, cast(attr_update))
            storage.all()[key].save()
        elif len(line) == 0:
            print("** class name missing **")
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, line):
        """Display number of instance specified"""
        args = parse(line)
        if len(line) == 0:
            print("** class name missing **")
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
        else:
            count = [key for key, val in storage.all().items()
                     if key.startswith(args[0] + ".")]
            print(len(count))

    def default(self, line):
        """
            Handles command with no method
        """
        try:
            args = line.split('.')
            cls_name = args[0]
            commands = args[1].replace('(', '')[:-1]
            cmd_name = commands.split('"')[0]

            if cmd_name == 'all':
                self.do_all(cls_name)
            elif cmd_name == 'count':
                HBNBCommand.count(cls_name)
            elif cmd_name == 'show':
                id = commands.split('"')[1]
                arg = ' '.join([cls_name, id])
                self.do_show(arg)
            elif cmd_name == 'destroy':
                id = commands.split('"')[1]
                arg = ' '.join([cls_name, id])
                self.do_destroy(arg)
            elif cmd_name == 'update':
                if '{' in commands:
                    id = commands.split('"')[1]
                    dict_d = commands.split('{')[1][:-1]
                    value = '{' + dict_d + '}'
                    dict_value = eval(value)
                    for k, v in dict_value.items():
                        if type(v) == int:
                            v = str(v)
                        v = '"' + v + '"'
                        arg = ' '.join([cls_name, id, k, v])
                        self.do_update(arg)
                else:
                    id = commands.split('"')[1]
                    attr = commands.split('"')[3]
                    value = commands.split(',')[2][1:]
                    arg = ' '.join([cls_name, id, attr, value])
                    self.do_update(arg)
            else:
                super().default(line)
        except Exception:
            super().default(line)


def parse(line):
    """Helper method to parse user typed input

    Returns
    -------
    tuple
        a list of user typed string
    """
    return tuple(line.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
