#!/usr/bin/python3
"""module that contains entry point to the command interpreter"""
import cmd
import re
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    @staticmethod
    def pattern(arg):
        """
        Retrieve the cmd method and the respective arguments according
        to a pattern so that they can be invoked under this scheme:
        <class>. <cmd> ([args, ...])
        """
        pattern = r'\.([^.]+)\(|([^(),]+)[,\s()]*[,\s()]*'
        argum = re.findall(pattern, arg)
        cmd = argum[0][0]
        argum = argum[1:]
        line = ' '.join(map(lambda x: x[1].strip('"'), argum))
        return cmd, line

    @staticmethod
    def pattern_handling(args):
        """deals with the splitting and arrangement of argument"""
        arg_list = []
        PATTERN = re.compile(r''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''')
        new_args = PATTERN.split(args)
        for arg in new_args:
            arg_list.append(arg.strip('"'))
        return arg_list

    @staticmethod
    def handle_arg(arg):
        """return key and other arguments"""
        new_arg = HBNBCommand.pattern_handling(arg)
        if len(new_arg) > 1:
            key = "{}.{}".format(new_arg[0], new_arg[1])
            return key, new_arg
        else:
            return new_arg[0], new_arg

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        return False

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it to
        json file and prints its id"""

        if arg:
            try:
                cls = models.classes[arg]
                new = cls()
                models.storage.save()
                print("{}".format(new.id))
            except (KeyError):
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """prints the string representation of an instance based on the
        class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            key, new_arg = self.handle_arg(arg)
            try:
                models.classes[new_arg[0]]
            except (KeyError):
                print("** class doesn't exist **")
                return

            if len(new_arg) == 1:
                print("** instance id missing **")
            else:
                try:
                    model = models.storage.all()[key]
                    print(model)
                except (KeyError):
                    print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id and save
        changes to file"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            key, new_arg = self.handle_arg(arg)
            if not models.classes.get(new_arg[0], False):
                print("** class doesn't exist **")
            else:
                if len(new_arg) == 1:
                    print("** instance id missing **")
                    return

                try:
                    models.storage.all().pop(key)
                    models.storage.save()
                except (KeyError):
                    print("** no instance found **")

    def do_all(self, arg):
        """prints all string representation of all instances based
        or not on the class name"""
        models_list = []
        if len(arg) == 0:
            for model in models.storage.all():
                models_list.append(str(models.storage.all()[model]))
            print(models_list)
        else:
            key, new_arg = self.handle_arg(arg)
            if not models.classes.get(new_arg[0], False):
                print("** class doesn't exist **")
            else:
                for model in models.storage.all():
                    if model.split(".")[0] == new_arg[0]:
                        models_list.append(str(models.storage.all()[model]))
                print(models_list)

    def do_update(self, arg):
        """updates an instance based on the class name and id by adding
        or updating attribute"""
        if len(arg) == 0:
            print("** class name is missing **")
        else:
            key, new_arg = self.handle_arg(arg)
            if not models.classes.get(new_arg[0], False):
                print("** class doesn't exist **")
                return
            else:
                if len(new_arg) >= 2:
                    if len(new_arg) == 2:
                        print("** attribute name missing **")
                        return

                    elif len(new_arg) % 2 == 1:
                        print("** value missing **")
                        return
                    else:
                        attr = new_arg[2::2]
                        value = new_arg[3::2]
                        try:
                            model_dict = models.storage.all().get(key)
                            model = models.classes.get(new_arg[0])
                            model = (model_dict)
                            for i in range(len(attr)):
                                setattr(model, attr[i], value[i])
                            model.save()
                        except (KeyError):
                            print("** no instance found **")
                            return

            if len(new_arg) == 1:
                print("** instance id missing **")
                return

    def do_BaseModel(self, arg):
        """
        Lets you invoke each of the console methods
        for the BaseModel class with the following syntax:
        BaseModel.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = self.pattern(arg)
        self.onecmd(' '.join([cmd, 'BaseModel', line]))

    def do_Amenity(self, arg):
        """
        Lets you invoke each of the console methods
        for the Amenity class with the following syntax:
        Amenity.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = self.pattern(arg)
        self.onecmd(' '.join([cmd, 'Amenity', line]))

    def do_City(self, arg):
        """
        Lets you invoke each of the console methods
        for the City class with the following syntax:
        City.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = self.pattern(arg)
        self.onecmd(' '.join([cmd, 'City', line]))

    def do_Place(self, arg):
        """
        Lets you invoke each of the console methods
        for the Place class with the following syntax:
        Place.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = self.pattern(arg)
        self.onecmd(' '.join([cmd, 'Place', line]))

    def do_Review(self, arg):
        """
        Lets you invoke each of the console methods
        for the Review class with the following syntax:
        Review.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = self.pattern(arg)
        self.onecmd(' '.join([cmd, 'Review', line]))

    def do_State(self, arg):
        """
        Lets you invoke each of the console methods
        for the State class with the following syntax:
        State.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = self.self.pattern(arg)
        self.onecmd(' '.join([cmd, 'State', line]))

    def do_User(self, arg):
        """
        Lets you invoke each of the console methods
        for the User class with the following syntax:
        User.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = self.pattern(arg)
        self.onecmd(' '.join([cmd, 'User', line]))

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
