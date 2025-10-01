import sys as __surely_not_even_close_to_sys

def _setup_path_from_packagefolder():
    import os, re
    from sys import path
    def replace_var(match):
        var_name = match.group(1)
        return os.environ[var_name]  # Fallback to original if not found

    # Regex to find ${...} and replace using the dictionary
    
    with open(".packagefolder", "a+t") as package_folder_file:
        package_folder_file.seek(0)
        for _line in reversed( package_folder_file.readlines() ):
            line = _line.strip()
            if not line: continue # skip empty lines
            if line.startswith("#"): continue # skip comments
            try:
                # fetch env, skip if env variable is not defined.
                enved_line = re.sub(r"\$\{([^}]+)\}", replace_var, line)
            except KeyError:
                continue
            # if already in there skip too.
            if enved_line in path: continue

            # ok, now insert.
            path.insert(0, enved_line )


_setup_path_from_packagefolder()
del _setup_path_from_packagefolder

for module_name in dir( __surely_not_even_close_to_sys ):
    locals()[ module_name ] = getattr( __surely_not_even_close_to_sys, module_name )

del __surely_not_even_close_to_sys