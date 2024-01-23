import os
from pathlib import Path

project_name = 'heart_disease_pred'


list_of_files = [
    
    '.github.workflows/.gitkeep'
    'requirements.txt',
    'setup.py',
    'schema.yaml',
    'test.py',
    'main.py',
    'app.py',
    'templates/index.html',
    'static/css/index.css',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/config_manager.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/commom.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/logger/__init__.py',
    f'src/{project_name}/exception/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    'research/trials.ipynb'
    
]

for filepath in list_of_files:
    filepath = Path(filepath)

    file_dir, file_name = os.path.split(filepath)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
    

    if (not os.path.exists(filepath))  or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass

    





