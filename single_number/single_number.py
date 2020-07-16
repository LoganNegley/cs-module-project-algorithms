'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # U
    # given a list of numbers find the number that doesn't appear twice
    # return that number that doesn't appear twice
    # P
    # loop throught list 
    # compare each num to see if any are the same
    # return the num that appears only once

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")