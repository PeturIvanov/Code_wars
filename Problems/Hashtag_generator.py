def generate_hashtag(s):
    if s:
        s = '#' + s.title().replace(' ', '')
        return s
    else:
        return False

