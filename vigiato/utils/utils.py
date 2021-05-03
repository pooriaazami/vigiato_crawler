def check_link(link: str):
    if link.startswith('https://'):
        return link.startswith('https://vigiato')

    return True
