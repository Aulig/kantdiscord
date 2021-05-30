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