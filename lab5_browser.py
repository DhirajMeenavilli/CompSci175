# ----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author:
# Collaborators/references:
# ----------------------------------------------------

from stack import Stack

def getAction():
    """
    This recives the action the user wishes to perform, and will wipe the forward stack
    Inputs: None
    Returns: User Action
    :return:
    """
    userWant = input('Enter  = (to enter a new website address), <(back button), > (forward button), or q to quit the browser simulation ')
    return userWant


def goToNewSite(current, bck, fwd):
    """
    This allows the user to view a new site
    Inputs: The current webpages, the back stack, and the forward stack
    Returns: the new website that is being looked at.
    :param current:
    :param bck:
    :param fwd:
    :return:
    """
    URL = input('What is the new website you would like to view. ')
    fwd.clear()
    fwd.push(URL)
    bck.push(current)
    return fwd.peek()


def goBack(current, bck, fwd):
    """
    This allows the user to go back to a website they had previously been on.
    Inputs: The current webpage, the back stack, and the forward stack.
    Returns: The website previous to the current one being viewed
    :param current:
    :param bck:
    :param fwd:
    :return:
    """
    try:
        page = bck.peek()
        bck.pop()
        fwd.push(current)
    except:
        page = current
    return page

def goForward(current, bck, fwd):
    """
    This function allows the user to go forward to a previously seen website
    Inputs: The current webpage being viewed, the back stack, and the forward stack
    Returns: The website that is ahead in the users history
    :param current:
    :param bck:
    :param fwd:
    :return:
    """
    try:
        page = fwd.peek()
        fwd.pop()
        bck.push(current)
    except:
        page = current
    return page


def main():
    """
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    :return:
    """
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()

    current = HOME
    quit = False

    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            if action != 'q' and action != '>' and action != '<' and action != '=':
                raise Exception("Invalid Entry.")

        except Exception as actionException:
            print(actionException.args[0])

        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            if action == '<':
                current = goBack(current,back,forward)
            if action == '>':
                current = goForward(current,back,forward)
            if action == 'q':
                quit = True

    print('Browser closing...goodbye.')


if __name__ == "__main__":
    main()

