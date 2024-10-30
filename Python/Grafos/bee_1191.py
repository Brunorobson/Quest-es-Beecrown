def post_order(pre_order, in_order):
    if not pre_order:
        return ""

    root = pre_order[0]
    root_index = in_order.index(root)

    left_in_order = in_order[:root_index]
    right_in_order = in_order[root_index + 1:]

    left_pre_order = pre_order[1:1 + len(left_in_order)]
    right_pre_order = pre_order[1 + len(left_in_order):]

    left_post_order = post_order(left_pre_order, left_in_order)
    right_post_order = post_order(right_pre_order, right_in_order)

    return left_post_order + right_post_order + root
import sys

for line in sys.stdin:
    line = line.strip()
    if line: 
        pre_order, in_order = line.split()
        print(post_order(pre_order, in_order))