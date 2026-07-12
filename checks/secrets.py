import re

def check_for_secrets(item, keywords):
    aws_pattern = r"AKIA[0-9A-Z]{16}"
    git_token_pattern = r"ghp_[A-Za-z0-9]{36}"

    try:
        text = item.read_text()
    except:
        return None

    for keyword in keywords:
        if keyword in text.lower():
            return item
    
    # Flag anything matching an AWS access key pattern using regex
    if re.search(aws_pattern, text):
        return item
    
    # Flag anything matching an GitHub token key pattern using regex
    if re.search(git_token_pattern, text):
        return item

    return None
