class VersionTarget:
    def __init__(self, diff_file:str):
        self.prev_version = None
        self.next_version = None
        self.diff_file = diff_file
    
    def get_version(self, line: str):
        if '=' in line:
            return line.split('=')[1].replace('"', '').replace("'","").strip()
        if ':' in line:
            return line.split(':')[1].replace('"', '').replace("'","").strip()

    def check_version_modified(self):
        with open(self.diff_file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if 'version' in line:
                    if line.startswith('+'):
                        self.next_version = self.get_version(line)
                    elif line.startswith('-'):
                        self.prev_version = self.get_version(line)
        
        if self.prev_version is None and self.next_version is None:
            return False
        elif self.prev_version is None and self.next_version is not None:
            self.prev_version = '0.0.0'
            return True
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
        else:
            try:
                if int(self.prev_version.split('.')[-1]) + 1 == int(self.next_version.split('.')[-1]):
                    return True
                else:
                    return False
            except:
                if self.prev_version < self.next_version:
                    return True
                else:
                    return False