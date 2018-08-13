import uuid


def get_filename(wtf):
    string = str(uuid.uuid4())
    return string + '.' + wtf.split('.')[-1]
