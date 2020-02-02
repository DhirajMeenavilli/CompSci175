# ----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program: To simulate browsing an internet search engine

# Title: Web Simulation
# Author:Dhiraj Meenavilli
# Date: 02/01/2020

# Collaborators/references: N/A
# ----------------------------------------------------

def getAction():
    """
    In getAction the user is asked to input whether they'd like to go forward, backward, quit, or to a new website, if they do not enter a valid string they are asked over and over until they do
    Inputs: None
    Returns: String
    :return:
    """
    valid = False
    while valid != True:
        userWant = input('Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
        if userWant != '=' and userWant != '<' and userWant != '>' and userWant != 'q':
            print('Invalid entry')
        else:
            valid = True
            return userWant


def goToNewSite(current, pages):
    """
    This function allows the user to input which website they'd like to go to, and appends it to the array as well as allows the user to view that page.
    Inputs: Current page, as well as the pages array
    Returns: The current index of the array which represents the site the user wishes to view.
    :param current:
    :param pages:
    :return:
    """
    valid = False
    while valid == False:
        URL = input("URL: ")
        if "www" not in URL:
            print("Unable to reach URL, try again.")
            valid = False
        else:
            pages.insert((current+1),URL)
            current += 1
            valid = True
            return current

def goBack(current, pages):
    """
    This function allows the user to go back a single web page
    Inputs: Current index value, and the websites array
    Returns: The index value pertaining to the next website in the array
    :param current:
    :param pages:
    :return:
    """
    if current > 0:
        current -= 1
    else:
        current = 0
        print("There are no previous websites")
    return current


def goForward(current, pages):
    """
    This function allows the user to go forward a single web page
    Inputs: Current index value, and the websites array
    Returns: The index value pertaining to the previous website in the array
    :param current:
    :param pages:
    :return:
    """
    noForward = current
    current += 1
    try:
        pages[current]
    except:
        print("There are no websites to go forward to")
        current = noForward
    return current


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    userActions = []
    currentIndex = 0
    quit = False

    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        userActions.append(action)

        if userActions[0] == '<' and userActions[1] == '=':
            websites = websites[0:(currentIndex+1)]

        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)

        elif action == '<':
            currentIndex = goBack(currentIndex, websites)

        elif action == '>':
            currentIndex = goForward(currentIndex, websites)

        elif action == 'q':
            quit = True

        if len(userActions) == 2:
            userActions.pop(0)

    print('Browser closing...goodbye.')


if __name__ == "__main__":
    main()
