#!/usr/bin/python3
'''the entry point of the command interpreter'''


from shlex import split

from models.base_model import BaseModel
'''the base model'''

import cmd
'''cmd model'''

from models import storage


class HBNBCommand(cmd.Cmd):
    '''the class of the command interpreter'''

    prompt = "(hbnb) "

    def emptyline(self):
        '''to skip the empty line'''

    def parse(self, strr):
        '''a function to parse the line and return a list of the arguments'''
        argv = strr.split()
        arg = list()
        s = ""
        i = 0
        for j in argv:
            if j[0] == '"' and j[len(j) - 1] == '"':
                arg.append(j)
            elif j[len(j) - 1] == '"':
                i = 0
                s += j
                s += " "
                arg.append(s)
                s = ""
            elif j[0] == '"':
                i += 1
                s += j
            else:
                if i == 0:
                    arg.append(j)
                else:
                    s += " "
                    s += j
        return arg


    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program'''
        return True
    
    def do_create(self, obj):
        '''Create command to creates a new instance of BaseModel and print the id'''
        if len(obj) == 0:
            print("** class name missing **")
        elif obj != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_ins = BaseModel()
            new_ins.save()
            print(new_ins.id)

    def do_show(self, arg):
        '''Show prints the string representation of an instance based on the class name and id'''
        lis = arg.split(" ", 2)
        if lis[0] == '':
            print("** class name missing **")
        elif lis[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(lis) < 2:
            print("** instance id missing **")
        else:
            o = 0
            store = storage.all()
            s = "{}.{}".format(lis[0], lis[1])
            for i in store:
                if i == s:
                    o = 1
                    print(store[s])
            if o == 0:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''Destroy deletes an instance based on the class name and id'''
        lis = arg.split(" ", 2)
        if lis[0] == '':
            print("** class name missing **")
        elif lis[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(lis) < 2:
            print("** instance id missing **")
        else:
            o = 0
            store = storage.all()
            s = "{}.{}".format(lis[0], lis[1])
            for i in store:
                if i == s:
                    o = 1
            if o == 0:
                print("** no instance found **")
            else:
                del store[s]
                storage.save()

    def do_all(self, obj):
        '''All prints all string representation of all instances based or not on the class name'''
        lis = list()
        if obj != "BaseModel":
            print("** class doesn't exist **")
        else:
            for i in storage.all().values():
                if obj == i.__class__.__name__:
                    lis.append(i.__str__())
            print(lis)

    def do_update(self, strr):
        '''Update updates an instance based on the class name and id by adding or updating attribute'''
        argv = self.parse(strr)
        store = storage.all()
        if len(argv) == 0:
            print("** class name missing **")
            return False
        elif argv[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        elif len(argv) < 2:
            print("** instance id missing **")
            return False
        else:
            o = 0
            s = "{}.{}".format(argv[0], argv[1])
            for i in store:
                if i == s:
                    o = 1
            if o == 0:
                print("** no instance found **")
                return False
            if len(argv) < 3:
                print("** attribute name missing **")
                return False
            elif len(argv) < 4:
                print("** value missing **")
                return False
            else:
                obj = store[s]
                obj.__dict__[argv[2]] = argv[3]
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
