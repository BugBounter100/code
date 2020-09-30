def parent_index(h,indx):
    max_indx = 2**h - 1
    if(max_indx < indx):
        return -1
    else:
        offset = 0
        flag = True
        size = max_indx
        result = -1
        while(flag):
            if(size == 0):
                flag == False
            size = size >> 1
            left_node = offset + size
            right_node = left_node + size
            my_node = right_node + 1
            if(left_node == indx) or (right_node == indx):
                result = my_node
                flag = False
            if(indx > left_node):
                offset = left_node
        return result
def solution(h, q):
    return [ parent_index(h,x) for x in q ]
