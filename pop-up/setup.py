from cx_Freeze import setup, Executable

base = None

executables = [Executable("popup.py", base=base)]

packages = ["idna", "datetime", "win10toast"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name = "<popup>",
    options = options,
    version = "<1.0>",
    description = '<pop up program>',
    executables = executables
)