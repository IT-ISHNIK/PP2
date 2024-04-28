from configparser import ConfigParser

def load_config(filename="0database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        print("Connected to DB")
    else:
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
    return db
    print(db)

load_config()