# Program for finding the grade of some text
def main():
    text = input("Text: ")
    grade = readability(text)
    if grade >= 1 and grade <= 16:
        print(f"Grade {grade}")
    elif grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")   

# Function for finding the grade
# By iterating over the text and counting each element
# And inputting the values in the coleman-liau index
def readability(text):
    letters, sentences, words = 0, 0, 1

    for char in text:
        if char == ' ':
            words += 1
        elif char in ['.', '!', '?']:
            sentences += 1
        elif char.isalpha():
            letters += 1

    avg_letters = letters / words * 100
    avg_sentences = sentences / words * 100

    grade = round(0.0588 * avg_letters - 0.296 * avg_sentences - 15.8)
    return grade

main()