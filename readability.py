# Program for finding the grade of some text
def main():
    """Uses the readability function to find the grade of the given text"""

    text = input("Text: ")
    grade = readability(text)
    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")   
    else:  
        print(f"Grade {grade}")


# Function to calculate the coleman-liau readability index of some text
# Outputs the estimated US grade level
def readability(text: str) -> int:
    """
    Calculates coleman-liau readability index of any given text

    Args:
        text (str): The text to find the grade of

    Returns:
        int: The grade of the text

    Raises:
        ValueError: If the string doesnt contain any characters or if it is only whitespace
    """
    
    if len(text) == 0 or text.isspace():
        raise ValueError("Input must contain a valid sentence.")
    
    letters = sum(1 
                  for char 
                  in text 
                  if char.isalpha())
    
    words = len(text.split())

    sentences = sum(1 
                    for char 
                    in text 
                    if char in ['.', '!', '?'])

    avg_letters = letters / words * 100
    avg_sentences = sentences / words * 100

    grade = round( 0.0588 
                  * avg_letters 
                  - 0.296 
                  * avg_sentences
                  - 15.8)
    return grade


main()