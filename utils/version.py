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
        prev_major, prev_minor, prev_build = self.prev_version.split('.')
        next_major, next_minor, next_build = self.next_version.split('.')
        if int(prev_major) + 1 == int(next_major):
            return True
        elif int(prev_major) == int(next_major) and int(prev_minor) + 1 == int(next_minor):
            return True
        elif 'a' in prev_build and 'a' in next_build:
            if int(prev_build.split('a')[1]) + 1 == int(next_build.split('a')[1]):
                return True
            else:
                return False
        elif 'b' in prev_build and 'b' in next_build:
            if int(prev_build.split('b')[1]) + 1 == int(next_build.split('b')[1]):
                return True
            else:
                return False
        elif 'rc' in prev_build and 'rc' in next_build:
            if int(prev_build.split('rc')[1]) + 1 == int(next_build.split('rc')[1]):
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