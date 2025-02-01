import pandas as pd
def get_user_input():
    # Initialize an empty list to store user input
    data = []
    
    # Get the number of elements from the user
    n = int(input("Enter number of elements: "))
    
    # Loop to get each element from the user
    for _ in range(n):
        ele = int(input("Enter element: "))
        data.append(ele)
    
    # Return the list of user input
    return data

def main():
    # Get the list of values from the user
    data = get_user_input()
    
    # Display the list of values without using pandas
    print('List of values without using pandas:')
    print(data)
    print()
    
    # Convert the list of values into pandas series
    series = pd.Series(data)
    print('Pandas Series:')
    print(series)

if __name__ == "__main__":
    main()
