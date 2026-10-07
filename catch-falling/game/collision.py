"""
collision: figures out whether a falling object is within the basket.
"""


def is_caught(basket_rect, obj):
    horizontal_overlap = basket_rect.left <= obj.x <= basket_rect.right
    vertical_overlap = obj.y + obj.radius >= basket_rect.top

    return horizontal_overlap and vertical_overlap