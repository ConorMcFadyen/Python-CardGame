import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class GUI(App):
  def generate_card(self):
    #Create the random card for the Dealer
    self.dealer_card = random.randint(2, 10)

    #Create the random card for the Player
    self.player_card = random.randint(2,10)

    # Compare both generated card, if they are the same regenerate the cards
    if self.player_card == self.dealer_card:
      print("Cards where the same , you'll get new cards")
      generate_card()

    return  self.dealer_card , self.player_card


  def lower(self , dealer_card , player_card):
    #When player Guesses lower button, compare the both cards and count if the player is correct

    # Tell the player they are correct or incorrect
    if dealer_card < player_card:
      print("true")
    else:
      print("false")

  def higher(self, dealer_card , player_card):
    #When player Guesses higher button, compare the both cards and count if the player is correct

    # Tell the player they are correct or incorrect
    if dealer_card > player_card:

      print("true")
    else:
      print("false")


  def build(self):
    #Create the GUI layout and we will only use one column
    self.window =GridLayout()
    self.window.cols = 1

    #create the cards by calling the generate function
    player_card , dealer_card = self.generate_card()

    #Display String of the players card
    player_str=str(player_card)
    self.greeting = Label(text = "Your Card is: " +player_str + "♦")
    self.window.add_widget(self.greeting)


    #Ask the user to guess a card
    self.greeting = Label(text = "Guess if the dealers Card is Higher or Lower")
    self.window.add_widget(self.greeting)

    #Display button to allow the user to guess lower , when clicked call the 'higher' function
    self.button_higher = Button(
      text="Higher",
      size_hint=(0.5, 0.3))
    self.button_higher.bind(on_press=lambda x:self.higher(dealer_card , player_card))
    self.window.add_widget(self.button_higher)

  # Display button to allow the user to guess lower , when clicked call the 'lower' function
    self.button_lower = Button(
      text="Lower",
      size_hint=(0.5, 0.3))
    self.button_lower.bind(on_press=lambda x: self.lower(dealer_card , player_card))
    self.window.add_widget(self.button_lower)



    return self.window



if __name__ == "__main__":
  GUI().run()
