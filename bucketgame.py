from random import shuffle
def shuffle_list(list_to_be_shuffled):
    shuffle(list_to_be_shuffled)
    return list_to_be_shuffled
def player_guess():
    guess =''
    while guess not in ['0','1','2']:
        guess = input('Enter a number : 0 , 1 or 2')
    return int(guess)
def check_guess(shuffled_list,guess1):
    if shuffled_list[guess1] == 'O':
        print('Your Guess is Right !')
    else:
        print('Your Guess is Wrong !')
        print(shuffled_list)
list1 = [' ','O',' ']
list2 = shuffle_list(list1)
num = player_guess()
check_guess(list2,num)