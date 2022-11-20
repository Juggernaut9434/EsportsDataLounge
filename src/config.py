from configparser import ConfigParser
import os

def config(filename="database.ini"):
    parser = ConfigParser()
    path = os.path.join(filename)
    parser.read(path)

    db = {}
    assert parser.has_section('postgresql'), f"Cannot find postgresql section in prodivded {filename}"
    params = parser.items('postgresql')

    for param in params:
        db[param[0]] = param[1]     # db['host'] = 'localhost'

    return db
