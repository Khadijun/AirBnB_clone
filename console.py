#!/usr/bin/python3
import cmd
'''
    This module defines class cmd
'''


class HBNBCommand(cmd.Cmd):
    ''' simple command processor: A subclass that inhherits from class Cmb. '''
    prompt = ' (hbnb)'

    def do_EOF(self, line):
        ''' Indicates End- of - line. '''
        return True

    def do_quit(self, line):
        ''' Quit command to exit the program '''
        return True

    def emptyline(self):
        ''' Do nothing on empty input line. '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
