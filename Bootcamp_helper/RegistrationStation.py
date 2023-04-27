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

    print('Username - Date - Location - Experience: 4 April - Johannesburg Physical - No prior experience')


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
    
    while True:
        username = input_user_name()
        info = ''
        data = read_file(file_name)

        for i in data:            
            split = i.split(' - ')
            if username == split[0]:
                for i in split[1:]:
                    info += i + ' - '
                info = info[:-3]
                print(info, end='')
                return info
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
