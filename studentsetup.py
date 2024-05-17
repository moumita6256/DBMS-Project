from cx_Freeze import *
includefiles = ["mana.ico.png"]
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "win32GUI"

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "StudentManagementSystemComplete",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\StudentManagementSystemComplete.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version="0.1",
    description="Student Management System Developed By Moumita Mowly",
    author="Moumita Mowly",
    name="Student Management System",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
         Executable(
             script="StudentManagementSystemComplete.py",
             base=base,
             icon='mana.ico.png',
         )
    ]
)
