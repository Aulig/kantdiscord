import urllib.parse


def url_prepare_string(input):
    if not input:
        return "_"
    else:
        return urllib.parse.quote(input)


def create_meme(top_text, bottom_text, background):
    return f"https://api.memegen.link/images/custom/{url_prepare_string(top_text)}/{url_prepare_string(bottom_text)}.png?background={background}"