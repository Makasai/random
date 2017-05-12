import pickle
import os

config_directory = '/Users/jkam/pylib/config_files/'

class ConfigDict(dict):

    def __init__(self, config_name):
        self._filename = config_directory + config_name + '.pickle'
        if not os.path.isfile(self._filename):
            with open(self._filename, 'w') as f:
                pickle.dump({}, f)
        with open(self._filename) as f:
            pkl = pickle.load(f)
            self.update(pkl)


    def __setitem__(self, key, val):
        print "Writing to dictionary"
        dict.__setitem__(self, key, val)
        test = self

        with open(self._filename, "w") as f:
            pickle.dump(test, f)

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            raise ConfigDictException(self, key)


class ConfigDictException(Exception):
    def __init__(self, config_dict, key):
        self.config_dict = config_dict
        self.key = key
    def __str__(self):
        return "There is no key named '%s'. Available keys: %s" %(self.key, ', '.join(self.config_dict.keys()))
