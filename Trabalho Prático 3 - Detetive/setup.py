import cx_Freeze

executables = [cx_Freeze.Executable('mainloop.py')]

cx_Freeze.setup(
    name="Mystery in Spacce",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['data']}},

    executables = executables
    
)