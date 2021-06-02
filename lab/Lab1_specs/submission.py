## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    left = 0
    right = x
    while(True):
        mid = left + (right - left) // 2
        if mid == left or mid == right:
            return mid
        if mid * mid == x:
            return mid
        if mid * mid > x:
            right = mid
        if mid * mid < x:
            left = mid


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    x_1 = x_0 - f(x_0) / fprime(x_0)
    iteration = 0
    while(abs(x_1 - x_0) > EPSILON and iteration < MAX_ITER):
        x_0 = x_1
        x_1 = x_0 - f(x_0) / fprime(x_0)
        iteration += 1
    return x_1


################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    tree_list = []
    tree_index = 0
    while('[' in tokens):
        for i in range(len(tokens)):
            if tokens[i] == ']':
                end_index = i
                break
        for i in range(len(tokens[:end_index])):
            if tokens[i] == '[':
                begin_index = i
        new_tree = Tree(tokens[begin_index - 1])
        for item in tokens[begin_index + 1 : end_index]:
            if type(item) != int:
                new_tree.add_child(Tree(item))
            else:
                new_tree.add_child(tree_list[item])
        tree_list.append(new_tree)
        part1 = tokens[:begin_index - 1] + [(tree_index)]
        part2 = tokens[end_index + 1:]
        tree_index += 1
        tokens = part1+part2

    return tree_list[-1]    # **replace** this line with your code

def max_depth(root): # do not change the heading of the function
    depth_dict = {}
    current_depth = 0
    if root:
        current_depth += 1
        depth_dict[current_depth] = root
    current_node = root
    current_children = root.children
    while(current_children):
        current_depth += 1
        depth_dict[current_depth] = current_children
        next_children = []
        for child in current_children:
            if child.children:
                for i in child.children:
                    next_children.append(i)
        current_children = next_children
    return max(depth_dict.keys())
