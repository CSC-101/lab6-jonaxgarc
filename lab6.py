import data
from typing import Optional
from data import Book

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[Book]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def selection_sort_books(bookList:list[Book]):
    length = len(bookList) #lenth of the book list

    for i in range(length): #goes through all indexes from 0-the length of the list
        initial_index = i #assumes the smallest index is i
        for j in range (i + 1,length): #iterates through the entire list and skips index 0
            # if the book list title is first in the alphabet initial index it replaces it
            if bookList[j].title <  bookList[initial_index].title:
                initial_index = j
        bookList[i], bookList[initial_index] = bookList[initial_index], bookList[i] #swaps the current one

# Part 2
def swap_case(original: str) -> str:
    swapped = []
    for i in original: # Takes every character from the original word
        if i.islower():
            swapped.append(i.upper())  # Swap lowercase to uppercase
        elif i.isupper():
            swapped.append(i.lower())  # Swap uppercase to lowercase
        else:
            swapped.append(i)  # Keep other characters unchanged
    return ''.join(swapped)  # Join the list into a string and return it
# Part 3
def str_translate(original: str, old: str, new: str) -> str:
    translated = []     # Makes an empty list to store the modified characters
    for i in original:     # Iterate through each character in the original string
        if i == old:
            translated.append(new)  # Replace old with new
        else:
            translated.append(i)  # Keep the character unchanged

    return ''.join(translated)     # Join the list into a string and return it

# Part 4
def histogram(input_string: str) -> dict:
    word_count = {} # Empty dictionary to store word counts

    words = input_string.split()  # Split the input string into words using space as the delimiter


    # Iterate through each word in the list of words
    for i in words:
        if i in word_count: # If the word is already in the dictionary, add to its count
            word_count[i] += 1
        else:
            word_count[i] = 1   # Or else add the word to the dictionary with a count of 1

    return word_count
