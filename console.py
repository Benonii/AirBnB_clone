#!/usr/bin/python3
'''the entry point of the command interpreter'''


from shlex import split

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State

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

    def checkClass(self, obj):
        '''a function to check if the obj's type is or is not in this list
            obj => the object
            Return: True if the obj's type exist, False if not
        '''
        classList = ["BaseModel", "User", "Place", "State",
                "City", "Amenity", "Review"]
        for i in classList:
            if obj == i:
                return True
        return False

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program'''
        return True
    
    def do_create(self, obj):
        '''Create command to creates a new instance of BaseModel and print the id'''
        argv = self.parse(obj)
        if len(argv) == 0:
            print("** class name missing **")
        elif self.checkClass(argv[0]) is not True:
            print("** class doesn't exist **")
        else:
            new_ins = eval(argv[0])()
            new_ins.save()
            print(new_ins.id)

    def do_show(self, arg):
        '''Show prints the string representation of an instance based on the class name and id'''
        argv = self.parse(arg)
        if len(argv) == 0:
            print("** class name missing **")
        elif self.checkClass(argv[0]) is not True:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            o = 0
            store = storage.all()
            s = "{}.{}".format(argv[0], argv[1])
            for i in store:
                if i == s:
                    o = 1
                    print(store[s])
            if o == 0:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''Destroy deletes an instance based on the class name and id'''
        argv = self.parse(arg)
        if len(argv) == 0:
            print("** class name missing **")
        elif self.checkClass(argv[0]) is not True:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            o = 0
            store = storage.all()
            s = "{}.{}".format(argv[0], argv[1])
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
        argv = self.parse(obj)
        if self.checkClass(argv[0]) is not True:
            print("** class doesn't exist **")
        else:
            for i in storage.all().values():
                if argv[0] == i.__class__.__name__:
                    lis.append(i.__str__())
            print(lis)

    def do_update(self, strr):
        '''Update updates an instance based on the class name and id by adding or updating attribute'''
        argv = self.parse(strr)
        store = storage.all()
        if len(argv) == 0:
            print("** class name missing **")
            return False
        elif self.checkClass(argv[0]) is not True:
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
