import cx_Freeze

executables = [cx_Freeze.Executable(script="src/main.py",
                                    targetName="BeanRPG.exe")]

include_files = ["src"]

packages = ["pygame",
            "os",
            "random",
            "json",
            "operator"]

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
