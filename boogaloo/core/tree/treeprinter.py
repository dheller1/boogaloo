def print_tree(tree):
    for node in tree.root:
        blanks = '  ' * (node.depth - 1) if node.depth > 1 else ''
        branches = '+- ' if node.depth > 0 else ''
        print(blanks + branches + str(node))
