"""
Registration Station project
"""
def read_file(file_name):

    """
    Read and return contents of text file
    """
    file = open(file_name, 'r')
    return file.readlines()


def input_user_name():

    """
    Takes username as input
    """
    username = input("Select username: ")
    return username    

def correct_or_incorrect():

    """
    Prompt to ask if details are correct or not
    @return correct or incorrect
    """
    prompt = input("Is this correct? (Y/n): ")

    return prompt

 
def correct_details():

    """
    Prompt to correct and write user details to text file, which includes:
    * Username
    * Date
    * Location
    * Experience
    """
    
    try:
        username = input('Select username: ')
        date = input('Enter date: ')
        location = input('Enter location: ')
        experience = input('Enter experience: ')
    except EOFError:
        pass
    
    new_str = f'{username} - {date} - {location} - {experience}'
    print(f'Is this correct? (Y/n): Username - Date - Location - Experience: {new_str}')
    
    # file = get_file_contents()
    
    # with open(file, 'r') as f:
    #     content = f.readlines()
    
    # # Find the line corresponding to the username
    # for line in content:
    #     if username in line:
    #         with open(file, 'w') as f:
    #             f.writelines(content)

def get_file_contents():

    """Return desired text file"""
    file = 'bootcampers.txt'
    return file

def find_username(file_name):

    """
    Main functiontion for running Registration Station, which inlcude:
       * get username input from user
       * check if username exists and print corresponding details
    @return corresponding information for username
       """
    
    """
    loop through each element in the file line by line and check if the first element is 
    equal to the username the user entered. If that is the case then extract the
    rest of the elements into a string.
    """
    while True:
        # get the username
        username = input_user_name()
        
        #create an empty string to later store the info
        info = ''
        
        #read the data inside the file
        data = read_file(file_name)
        
        #iterate through that data
        for i in data:
            # split the current element at each occurence of the string (' - ')            
            split = i.split(' - ')
            
            # check if the first element is equal to the username
            if username == split[0]:
                #iterate through the rest of the elements and concatenate them into a string
                for i in split[1:]:
                    info += i + ' - '
                #remove the last 3 elements (' - ')
                info = info[:-3]
                print(info, end='')
                return info
            
            #if the username is not found then print the following
        print('Please enter valid existing username')
        
   


if __name__ == "__main__":
    registrations_file = get_file_contents()
    information = find_username(registrations_file)
    while True:
        answer = correct_or_incorrect()
        if answer == "correct":
            print(information)
            break
        else:
            correct_details()
