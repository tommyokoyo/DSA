def binary_to_deciaml(binary):
    if not binary:
        return 0

    binary_number = 0
    current_node = binary

    while current_node is not None:
        binary_number = binary_number * 2 + current_node.data
        current_node = current_node.next

    return binary_number
