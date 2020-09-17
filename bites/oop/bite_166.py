import configparser
import re

class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        config = configparser.ConfigParser()
        config.read(ini_file)
        self.content = config

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
        """
        return len(self.content.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        env_list = self.content['tox']['envlist']
        env_list = re.sub(r'\n|,', ' ', env_list)
        return [e for e in env_list.split(' ') if e]
        # return [e.strip() for e in self.content['tox']['envlist'].strip().split(',') if e]

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        result = set()
        for section in self.content.sections():
            try:
                pyt_v = self.content.get(section, 'basepython')
                result.add(pyt_v)
            except:
                continue
        return result
