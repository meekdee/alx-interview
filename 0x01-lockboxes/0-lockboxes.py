#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    # Initialize a set to keep track of unlocked boxes
    unlocked_boxes = set()
    unlocked_boxes.add(0)  # The first box is initially unlocked

    # List to keep track of keys we have
    keys = list(boxes[0])

    # Iterate through the keys we have
    while keys:
        key = keys.pop()  # Get a key
        if key not in unlocked_boxes and key < len(boxes):
            unlocked_boxes.add(key)  # Unlock the box with the current key
            keys.extend(boxes[key])  # Add new keys from the unlocked box

    # Check if all boxes are unlocked
    return len(unlocked_boxes) == len(boxes)

# Testing the function
"""
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Should print True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Should print True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Should print False
"""
