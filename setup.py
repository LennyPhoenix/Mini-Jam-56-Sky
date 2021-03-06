import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages=["engine", "source",
                              "pymunk", "pyglet"], excludes=[])

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('main.py', base=base,
               targetName='RDR', icon="icon.ico")
]

setup(name='Run, Doughnut, Run!',
      version='1.0',
      description='Run!',
      options=dict(build_exe=buildOptions),
      executables=executables)
