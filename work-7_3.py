import os, shutil

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.rsplit('.', maxsplit=1)[-1] == 'html':
            dir_name = os.path.join('.\\my_project\\templates', os.path.basename(os.path.dirname(os.path.dirname(root))))
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            file_name = os.path.join(dir_name, file)
            if not os.path.exists(file_name):
                shutil.copy2(os.path.join(root, file), file_name)

