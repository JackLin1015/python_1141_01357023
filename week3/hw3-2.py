def tree_height(pre_order, in_order):
    if not pre_order or not in_order: 
        return 0
    root = pre_order[0]
    part = in_order.index(root)
    in_l = in_order[:part]
    in_r = in_order[part+1:]
    pre_l = pre_order[1:1+len(in_l)]
    pre_r = pre_order[1+len(in_l):]
    h_l = tree_height(pre_l, in_l)
    h_r = tree_height(pre_r, in_r)
    return 1 + max(h_l, h_r)

pre_order = list(map(int,input().split()))
in_order = list(map(int,input().split()))
print(tree_height(pre_order, in_order))



