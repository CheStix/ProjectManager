import os
import json

settingsFileName = 'projectManagerFileName.json'


class settingsClass(object):
    def __init__(self):
        self.path = os.path.join(os.path.expanduser('~'), settingsFileName)
        if not os.path.exists(self.path):
            self.makeDefault(self.path)

    def makeDefault(self, path):
        defData = dict(
            path=''
        )
        with open(path, 'w') as f:
            json.dump(defData, f, indent=4)

    def load(self):
        return json.load(open(self.path))

    def save(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)


