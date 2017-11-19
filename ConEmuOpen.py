import os, sublime, sublime_plugin

class ConEmuOpenCommand():
    def get_project(self):

        project_dir = os.path.dirname(self.window.active_view().file_name())
        full_path = project_dir.split("\\")       
        heredir = project_dir
        title = project_dir
        find_root = ''
        cont = 0
        while (cont < len(full_path)): # Check backwards
            find_root += full_path[cont] + "\\"
            if os.path.isdir(find_root + ".git"):
                heredir = find_root
                title = "PROJECT: " + full_path[cont] +" | ROOT: " + heredir
                break
            cont += 1

        return (project_dir, heredir, title)

    def open_conemu(self, dirname, title, launch_type):        

        if (launch_type == "cmd_new_window") or (launch_type == "sidebar_menu"): # CMD + New Windows OR Sidebar Menu
            command = "start conemu.exe /NoSingle -run {cmd::Cmder} -new_console:d:\""+dirname+"\" -new_console:t:\""+title+"\""

        elif launch_type == "cmd_new_tab": # CMD + Tabs
            command = "start conemu.exe /Single -run {cmd::Cmder} -new_console:d:\""+dirname+"\" -new_console:t:\""+title+"\""

        elif launch_type == "ps_new_window": # PoewrShell + New Windows
            command = "start conemu.exe /NoSingle -run {Powershell::Powershell} -new_console:d:\""+dirname+"\" -new_console:t:\""+title+"\""

        elif launch_type == "ps_new_tab": # PoewrShell + Tabs
            command = "start conemu.exe /Single /Dir \""+dirname+"\" -run {Powershell::Powershell} -new_console:d:\""+dirname+"\" -new_console:t:\""+title+"\""
        
        elif launch_type == "legacy": # Legacy
            command = "start conemu.exe /Single /Dir \""+dirname+"\" /cmdlist powershell -new_console:t:\""+title+"\""

        else:
            command = "cmd /C msg %username% ConEmuOpen - Error: launch_type unknown"
             
        os.system(command)

# open project folder
class OpenConemuProjectCommand(sublime_plugin.WindowCommand, ConEmuOpenCommand):
    def run(self, launch_type=[]):
        project_dir, heredir, title = self.get_project()
        if not project_dir:
            return

        self.open_conemu(heredir, title, launch_type[0])

# open "here" folder
class OpenConemuHereCommand(sublime_plugin.WindowCommand, ConEmuOpenCommand):
    def run(self, paths=[], launch_type=[]):
        project_dir, heredir, title = self.get_project()
        if not project_dir:
            return

        if paths:
            heredir = paths[0]
            if os.path.isfile(heredir):
                heredir = os.path.dirname(heredir)
        else:
            heredir = project_dir
            title = title
        
        self.open_conemu(heredir, title, launch_type[0])
