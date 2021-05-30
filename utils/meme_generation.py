def create_meme(top_text, bottom_text, background):

    if not top_text:
        top_text = "_"

    if not bottom_text:
        bottom_text = "_"

    bottom_text = bottom_text.replace(" ", "_")
    top_text = top_text.replace(" ", "_")

    return f"https://api.memegen.link/images/custom/{top_text}/{bottom_text}.png?background={background}"