import cx_Freeze

executables = [cx_Freeze.Executable(script="src/main.py",
                                    icon="src/resources/icon.ico",
                                    targetName="Tim's Adventure.exe")]

include_files = ["src"]

packages = ["pygame",
            "os",
            "random",
            "json",
            "operator",
            "logging",
            "shutil"]

excludes = ["tkinter",
            "numpy",
            "OpenGL",
            "html",
            "http",
            "email",
            "multiprocessing",
            "urllib",
            "xml",
            "socket"]

cx_Freeze.setup(
    name="Bean RPG",
    options={
        "build_exe": {
            "packages": packages,
            "excludes": excludes,
            "include_files": include_files
        }
    },
    executables=executables
)
