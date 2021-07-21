from PIL import Image

from utils.url_utils import url_prepare_string


def create_meme(top_text, bottom_text, background):
    return f"https://api.memegen.link/images/custom/{url_prepare_string(top_text)}/{url_prepare_string(bottom_text)}.png?background={background}"


def is_image(file):
    try:
        img = Image.open(file)
        img.verify()
        return True
    except Exception:
        return False


def is_video(file_name):
    # only video extensions discord will embed
    video_file_extensions = (".webm", ".mp4", ".gif", ".gifv")
    return file_name.endswith(video_file_extensions)


def check_image_nsfw(file_path):
    # result = classifier.classify(file_path)
    #
    # return {"safe": 1, "unsafe": 0} if len(result) == 0 else result[file_path]
    pass


def _average_video_nsfw_score(preds):

    safe = 0
    unsafe = 0

    for _, frame_result in preds.items():
        safe += frame_result["safe"]
        unsafe += frame_result["unsafe"]

    return {"safe": safe / len(preds), "unsafe": unsafe / len(preds)}



def check_video_nsfw(file_path):
    # result = classifier.classify_video(file_path)
    #
    # return {"safe": 1, "unsafe": 0} if len(result) == 0 else _average_video_nsfw_score(result["preds"])
    pass