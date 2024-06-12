import os
import yaml


def read_data_from_yaml(file_path):
    f = open(file_path, "r", encoding="utf-8")
    # res = yaml.load(f, yaml.FullLoader)
    res = yaml.full_load(f)
    return res


if __name__ == '__main__':
    cases = read_data_from_yaml(os.getcwd() + r'\case.yaml')
    print(cases)