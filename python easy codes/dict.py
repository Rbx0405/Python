def create_dictionary_by_first_char(input_string):
    """
    Creates a dictionary where the keys are the first characters of words,
    and the values are lists of words that start with those characters.
    
    :param input_string: A string containing multiple words.
    :return: A dictionary grouping words by their first character.
    """
    # Split the input string into words
    words = input_string.split()
    
    # Initialize an empty dictionary to store the results
    result_dict = {}
    
    # Loop through each word in the list
    for word in words:
        # Get the first character of the word
        first_char = word[0]
        
        # Check if the first character is already a key in the dictionary
        if first_char in result_dict:
            # If it is, append the word to the list of words
            result_dict[first_char].append(word)
        else:
            # Otherwise, create a new entry with the first character as key
            result_dict[first_char] = [word]
    
    return result_dict

# Example usage:
input_string = "apple banana apricot cherry blueberry cat"
print(create_dictionary_by_first_char(input_string))
