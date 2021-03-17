import yaml, os

with open('config.yaml') as f:
    templates = yaml.safe_load(f)

print(templates)

# Очень хотелось попробовать собственную рекурсию
def maker(path, args):
    if isinstance(args, dict):
        for folder in args.keys():
            if not os.path.exists(os.path.join(path, folder)):
                os.mkdir(os.path.join(path, folder))
            maker(os.path.join(path, folder), args[folder])
    elif isinstance(args, list):
        for file in args:
            maker(path, file)
    else:
        if not os.path.exists(os.path.join(path, args)):
            open(os.path.join(path, args), "w").close()


maker('', templates)
