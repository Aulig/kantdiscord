import random
from asyncio import sleep

CAPTION_SPLIT_CHAR = "|"


def _find_split_index(input):
    half_length = len(input) // 2

    potential_indices = [pos for pos, char in enumerate(input) if char == " "]

    if len(potential_indices) == 0:
        return len(input)

    # sort by which index has the smallest distance to half_length
    potential_indices.sort(key=lambda x: abs(x - half_length))

    return potential_indices[0]


def split_text(input):
    split_index = input.find(CAPTION_SPLIT_CHAR)

    if split_index == -1:
        split_index = _find_split_index(input)

    return input[:split_index], input[split_index + 1:]


async def send_words_slowly(words, channel):
    """ might mess up your word list (shuffle) """

    random.shuffle(words)

    msg = await channel.send(words[0])

    await sleep(4)

    for i in range(len(words) - 1):
        old_word = words[i]
        for j in range(len(old_word), 1, -1):
            await msg.edit(content=old_word[:j])
            await sleep(0.5)

        new_word = words[i + 1]
        for k in range(1, len(new_word), 2):
            await msg.edit(content=new_word[:k])
            await sleep(0.5)

        await sleep(4)

    await msg.delete()