import _md5


def hashlib_md5(msg):
    password_md5 = _md5.md5(msg.encode("utf-8")).hexdigest()
    return password_md5
