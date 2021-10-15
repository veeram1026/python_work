# Simple game for checking is there the guess correct ?

class GuessGame():
    
    def __init__(self,number,minimum=0,maximum = 100):
        """ This is the constructor of the GuessGame class.
        
        Args:
            number (int): number to guess
            minimum (int, optional): . Defaults to 0.
            maximum (int, optional): . Defaults to 100.
        """
        self.number = number
        self.guesses = 0
        self.minimum = minimum
        self.maximum = maximum
    
    def get_guess(self):
        """This function will get the gessed number from the user

        Returns:
            (int): user guessed number(valid)
        """
        while True:
            try:
                guessed = int(input(f'Enter a value between {self.minimum}-{self.maximum} : '))
                if self.minimum <= guessed >= self.maximum :
                    print(f'Please,enter a value between {self.minimum}-{self.maximum}')
                    continue
                return guessed
            except :
                print('Please enter a number')
                continue
        
    def play_game(self):
        """ This is the main function to paly the guess game.
        """
        while True:
            self.guesses +=1 
            guess = self.get_guess()
            if guess == self.number :
                print(f'Wow! your are guessed the number {self.number} at {self.guesses} guesses !')
                break
            elif guess < self.number :
                print('your are under the guess')
            else :
                print('your are over the guess')

#creating instance of the GuessGame class and calling play gane function to p
GuessGame(12).play_game()
          