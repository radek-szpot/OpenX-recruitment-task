def length_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters in the given string `s`.

    Parameters:
    s (string): string witch will be analyzed to find longest substring
    Returns:
    int: length of the longest substring
    """
    if not isinstance(s, str):
        raise TypeError
    # create dictionary to store found substrings in pairs {"substring":len(substring)}
    substrings_dict = dict()
    # create list to store characters appeared in substrings
    unique_list = list()
    # create iterator to control for loop
    substring_iter = 0
    while substring_iter != len(s):
        for char in s[substring_iter:]:
            if char not in unique_list:
                unique_list.append(char)
            else:
                # add to dictionary
                # key   -> elements from list into string
                # value -> length of parsed elements
                substrings_dict["".join(unique_list)] = len(unique_list)
                # add 1 to iterator to start for loop from next character
                unique_list.clear()
                substring_iter += 1
                break

    # return max value in substrings_dict
    return substrings_dict[max(substrings_dict, key=substrings_dict.get)]
