# This is a sample commands.py.  You can add your own commands here.
#
# Please refer to commands_full.py for all the default commands and a complete
# documentation.  Do NOT add them all here, or you may end up with defunct
# commands when upgrading ranger.

# A simple command for demonstration purposes follows.
# -----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)

# You can import any python module as needed.
import os
from os import system
import subprocess
from xml.etree.ElementTree import tostring

# You always need to import ranger.api.commands here to get the Command class:
from ranger.api.commands import Command


# Any class that is a subclass of "Command" will be integrated into ranger as a
# command.  Try typing ":my_edit<ENTER>" in ranger!
class my_edit(Command):
    # The so-called doc-string of the class will be visible in the built-in
    # help that is accessible by typing "?c" inside ranger.
    """:my_edit <filename>

    A sample command for demonstration purposes that opens a file in an editor.
    """

    # The execute method is called when you run this command in ranger.
    def execute(self):
        # self.arg(1) is the first (space-separated) argument to the function.
        # This way you can write ":my_edit somefilename<ENTER>".
        if self.arg(1):
            # self.rest(1) contains self.arg(1) and everything that follows
            target_filename = self.rest(1)
        else:
            # self.fm is a ranger.core.filemanager.FileManager object and gives
            # you access to internals of ranger.
            # self.fm.thisfile is a ranger.container.file.File object and is a
            # reference to the currently selected file.
            target_filename = self.fm.thisfile.path

        # This is a generic function to print text in ranger.
        self.fm.notify("Let's edit the file " + target_filename + "!")

        # Using bad=True in fm.notify allows you to print error messages:
        if not os.path.exists(target_filename):
            self.fm.notify("The given file does not exist!", bad=True)
            return

        # This executes a function from ranger.core.acitons, a module with a
        # variety of subroutines that can help you construct commands.
        # Check out the source, or run "pydoc ranger.core.actions" for a list.
        self.fm.edit_file(target_filename)

    # The tab method is called when you press tab, and should return a list of
    # suggestions that the user will tab through.
    # tabnum is 1 for <TAB> and -1 for <S-TAB> by default
    def tab(self, tabnum):
        # This is a generic tab-completion function that iterates through the
        # content of the current directory.
        return self._tab_directory_content()


class code(Command):
    """
    :code <file/directory>

    Opens a file or directory in VSCode
    """
    def execute(self):
        if self.arg(1):
            target_filename = self.rest(1)
        else:
            target_filename = self.fm.thisfile.path

        self.fm.notify("Opening " + target_filename + "...")

        if not os.path.exists(target_filename):
            self.fm.notify("The given file does not exist!", bad=True)
            return

        self.fm.run(['code', target_filename])

    def tab(self, tabnum):
        content = self._tab_directory_content()
        self.fm.notify(content)
        return content

class xcopy(Command):
    """
        :xcopy <file>
        Copies the file to clipboard (usefull for move files between aplications)
    """
    def execute(self):
        target_filename = []
        if self.arg(1):
            target_filename = self.rest(1)

            if not os.path.exists(target_filename):
                self.fm.notify("The given path does not exist!", bad=True)
                return
        else:
            target_filename = ' '.join([str(getattr(f, 'path')) for f in self.fm.thistab.get_selection()])

            for f in self.fm.thistab.get_selection():
                if not os.path.exists(str(getattr(f, 'path'))):
                    self.fm.notify("The given path does not exist!", bad=True)
                    return

        system('xclip-copyfile ' + target_filename)
        self.fm.notify('Copied files!')

    def tab(self, tabnum):
        content = self._tab_directory_content()
        self.fm.notify(content)
        return content

class myecho(Command):
    def execute(self):
        if self.arg(1):
            target_filename = self.rest(1)
        else:
            # target_filename = self.fm.thisfile.path
            target_filename = [getattr(f, 'path') for f in self.fm.thistab.get_selection()]
        self.fm.notify(target_filename)
        self.fm.run(['echo', ' '.join(target_filename)])

    def tab(self, tabnum):
        content = self._tab_directory_content()
        self.fm.notify(content)
        return content


class xpaste(Command):
    """
        :xpaste <file>
        Pastes the file to clipboard (usefull for move files between aplications)
    """
    def execute(self):
        self.fm.notify("Pasting files...")

        self.fm.run(['xclip-pastefile'])

    def tab(self, tabnum):
        content = self._tab_directory_content()
        self.fm.notify(content)
        return content

class fasd(Command):
    """
    :fasd

    Jump to directory using fasd
    """
    def execute(self):
        args = self.rest(1).split()
        if args:
            directories = self._get_directories(*args)
            if directories:
                self.fm.cd(directories[0])
            else:
                self.fm.notify("No results from fasd", bad=True)

    def tab(self, tabnum):
        start, current = self.start(1), self.rest(1)
        for path in self._get_directories(*current.split()):
            yield start + path

    @staticmethod
    def _get_directories(*args):
        import subprocess
        output = subprocess.check_output(["fasd", "-dl"] + list(args), universal_newlines=True)
        dirs = output.strip().split("\n")
        dirs.sort(reverse=True)  # Listed in ascending frecency
        return dirs