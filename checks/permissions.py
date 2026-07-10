import stat

def check_permissions(item):
    if not item.is_file():
        return None
    if item.stat().st_mode & stat.S_IWOTH:
        return item
    return None