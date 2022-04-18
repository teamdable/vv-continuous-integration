class VersionTarget:
    def __init__(self, diff_file:str):
        self.prev_version = None
        self.next_version = None
        self.diff_file = diff_file
    
    def get_version_string(self):
        if self.diff_file == '.version.diff':
            return ('__version__', '=')
        elif self.diff_file == '_version.py.diff':
            return ('__version__', '=')
        elif self.diff_file == 'package.json.diff':
            return ('version', ':')
        else:
            return ('unknown', '==')

    def check_version_modified(self):
        with open(self.diff_file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                version_string, split_target = self.get_version_string()
                if line.startswith("-" + version_string):
                    self.prev_version = line.split(split_target)[1].replace('"', '').replace("'","").strip()
                if line.startswith("+" + version_string):
                    self.next_version = line.split(split_target)[1].replace('"', '').replace("'","").strip()
        
        if self.prev_version is None or self.next_version is None:
            return False
        else:
            return True

    def check_version_update(self):
        if 'a' in self.prev_version and 'a' in self.next_version:
            if int(self.prev_version.split('a')[1]) + 1 == int(self.next_version.split('a')[1]):
                return True
            else:
                return False
        elif 'b' in self.prev_version and 'b' in self.next_version:
            if int(self.prev_version.split('b')[1]) + 1 == int(self.next_version.split('b')[1]):
                return True
            else:
                return False
        elif 'rc' in self.prev_version and 'rc' in self.next_version:
            if int(self.prev_version.split('rc')[1]) + 1 == int(self.next_version.split('rc')[1]):
                return True
            else:
                return False
        elif self.prev_version < self.next_version:
            return True
        else:
            return False