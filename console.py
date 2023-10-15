#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    
    prompt = "(hbnb) "
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """Exit on EOF (Ctrl-D)"""
        return True
    
    def emptyline(self):
        pass
    
    def default(self, line):
        """
        Default behavior to handle custom commands.
        Available commands: create, show, destroy, all, update
        """
        split_line = line.split()
        if len(split_line) == 0:
            return

        command = split_line[0]
        args = split_line[1:]

        if command == "create":
            self.do_create(args)
        elif command == "show":
            self.do_show(args)
        elif command == "destroy":
            self.do_destroy(args)
        elif command == "all":
            self.do_all(args)
        elif command == "update":
            self.do_update(args)
        else:
            print("** Invalid command **")
            
    def do_create(self, args):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes():
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
            
    def do_show(self, args):
        """Show the string representation of an instance."""
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            objects = storage.all()
            key = args[0] + "." + obj_id
            obj = objects.get(key, None)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)
    
    def do_destroy(self, args):
        """Delete an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            objects = storage.all()
            key = args[0] + "." + obj_id
            obj = objects.get(key, None)
            if obj is None:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()
    
    def do_all(self, args):
        """Print the string representation of all instances."""
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] in self.valid_classes():
            print([str(obj) for key, obj in objects.items() if key.split(".")[0] == args[0]])
        else:
            print("** class doesn't exist **")
            
    def do_update(self, args):
        """Update an instance based on class name, id, attribute, and value."""
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]

            objects = storage.all()
            key = class_name + "." + obj_id
            obj = objects.get(key, None)
            if obj is None:
                print("** no instance found **")
            else:
                try:
                    attr_type = type(getattr(obj, attribute_name))
                    setattr(obj, attribute_name, attr_type(attribute_value))
                    obj.save()
                except AttributeError:
                    print("** invalid attribute name **")
                except ValueError:
                    print("** invalid value **")
        
    def valid_classes(self):
        """
        Returns a list of valid class names from the available model classes.
        You can add more model classes as needed.
        """
        return ["BaseModel"]
    

if __name__ == '__main__':
    HBNBCommand().cmdloop() 
