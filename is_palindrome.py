def is_palindrome(input_string: str) -> bool:
    # Clean the input string
    # Remove non-alphanumeric characters
    # Convert to lowercase
    string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Check if string reads the same forward and backward
    return string == string[::-1]

# Test the function
input_str = "A man, a plan, a canal, Panama"
print(input_str)
print(f"Is it a palindrome?: { is_palindrome(input_str)}")
