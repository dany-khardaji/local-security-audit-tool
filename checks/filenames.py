def check_filenames(item, keywords):
    for keyword in keywords:
        if keyword in item.name.lower():
            return item
        
    if item.name.endswith((".key", ".pem")):
        return item
    return None