import os
import re
import importlib

def import_classes(module: str) -> None:
    module_name = module.split('.')[0]

    with open(os.path.join(os.path.dirname(__file__), module)) as scene_file:
        lines = scene_file.readlines()

    for line in lines:
        match = re.match(r'class ([a-zA-Z0-9]+)\(', line)
        if match:
            class_name = match.group(1)
            imported_module = importlib.import_module(f'.{module_name}', package=__name__)
            class_obj = getattr(imported_module, class_name)
            globals()[class_name] = class_obj

files = list(filter(lambda x: x.endswith('.py') and x != '__init__.py', os.listdir(os.path.dirname(__file__))))

print(f'Importing classes from {files}')
for file in files:
    import_classes(file)