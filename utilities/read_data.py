import pdb

import yaml


def getYamlData(filename, section='default_data'):
    with open(filename) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    if section.__contains__('default'):
        return data['default_data']
    return data[section]

