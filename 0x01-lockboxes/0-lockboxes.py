#!/usr/bin/python3
"""
Checks if all boxes can be unlocked

Functions:
    canUnlockAll: Check if all the boxes can be
                unlocked after getting the keys

    OpenBox: Recursive Funtion to open each boxes as keys are found
"""


def canUnlockAll(box_list):
    """
    canUnlockAll: Check if all the boxes can be
                unlocked after getting the keys

    Args:
        boxess: list -> Nested list of keys in all boxes
    """

    keys = [0]
    openBox(box_list, keys, 0, 0)
    return len(boxes) == len(keys)


def openBox(boxes, keys, key_index, index):
    """
    OpenBox: Open each boxes and store the keys found in there

    Args:
        boxes: the list of boxes
        keys: the list of keys found so far sorted according to find
        key_index: the next key to use to open box
        index: the index of the search
    """
    if index >= len(boxes):
        return

    keys.extend([elem for elem in boxes[key_index] if elem not in keys])
    if len(keys) <= index + 1:
        return
    return openBox(boxes, keys, keys[index + 1], index + 1)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))