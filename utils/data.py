import yaml


class Data(object):
    def __init__(self, file_path):
        self.file_path = file_path

    @property
    def data(self):
        with open(self.file_path, encoding='utf-8') as f:
            return yaml.safe_load(f)


if __name__ == '__main__':
    d = Data(r'D:\18期\longteng18\data\data.yaml')
    print(d.data)