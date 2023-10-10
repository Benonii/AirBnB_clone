#!/usr/bin/python3
'''the entry point of the command interpreter'''


import cmd
'''cmd model'''

class HBNBCommand(cmd.Cmd):
    '''the class of the command interpreter'''

    prompt = "(hbnb) "
    def emptyline(self):
        '''to skip the empty line'''
        
    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program'''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
