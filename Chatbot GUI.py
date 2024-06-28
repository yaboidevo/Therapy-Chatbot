import datetime
import random
import tkinter as tk
from tkinter import scrolledtext
import tkinter.font as font
from tkinter import Canvas
import requests
import sys



colors = ["black", "white", "red", "green", "yellow", "blue", "brown", "orange", "pink", "purple", "grey"]
ops = ['+', '-', '*', '/']
jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "What's an egg's favorite vacation spot? New Yolk City.",
    "Why couldn't the bicycle stand up by itself? It was two tired.",
    "What's a ninja's favorite type of shoes? Sneakers.", 
    "What do dentists call their x-rays? Tooth Picks!",
    "Did you hear about the first restaurant to open on the moon? It had great food, but no atmosphere!",
    "You heard the rumor going around about butter? Never mind, I shouldn’t spread it."]
animals = ["dog", "cow", "cat", "horse",
           "donkey", "tiger", "lion", "panther",
           "leopard", "cheetah", "bear", "elephant",
           "polar bear", "turtle", "tortoise", "crocodile",
           "rabbit", "porcupine", "hare", "hen",
           "pigeon", "albatross", "crow", "fish",
           "dolphin", "frog", "whale", "alligator",
           "eagle", "flying squirrel", "ostrich", "fox",
           "goat", "jackal", "emu", "armadillo",
           "eel", "goose", "wolf",
           "beagle", "gorilla", "chimpanzee", "monkey",
           "beaver", "orangutan", "antelope", "bat",
           "badger", "giraffe", "crab", "panda",
           "hamster", "cobra", "hammerhead shark", "camel",
           "hawk", "deer", "chameleon", "hippopotamus",
           "jaguar", "chihuahua", "king cobra", "ibex",
           "lizard", "koala", "kangaroo", "iguana",
           "llama", "chinchillas", "dodo", "jellyfish",
           "rhinoceros", "hedgehog", "zebra", "possum",
           "wombat", "bison", "bull", "buffalo",
           "sheep", "meerkat", "mouse", "otter",
           "sloth", "owl", "vulture", "flamingo",
           "racoon", "croc"]


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "imperial"}  # Specify units as imperial for Fahrenheit
    
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None


class ChatBot:
    def __init__(self):
        self.user_response = ''
        self.bot_response = ''

    def ask_question(self, question):
        self.user_response = question.lower()

    def generate_response(self):
        api_key = '8e090ef93ef571938d58ffe34f52bbc7'
        city = "Atlanta"
        weather_data = get_weather(api_key, city)
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        if self.user_response == " ":
            pass
        
        elif 'weather' in self.user_response:
            self.bot_response = "Look out the window."
            return(f"The weather in {city} today is {description} with a temperature of {temperature}°F.")
        

        elif "bye" in self.user_response or "exit" in self.user_response:
           self.bot_response = "Goodbye! It was nice chatting with you!"
           return(self.bot_response)  
           
           
        
        elif self.user_response == "hi" or "hello" in self.user_response or "hey" in self.user_response:
            self.bot_response = "Hello!"
        elif "got to" in self.user_response or "excit" in self.user_response or "cool" in self.user_response or "just" in self.user_response or "nice" in self.user_response or "amazing" in self.user_response:
                self.bot_response = "Good for you!"
    #mental health
                
        elif "feel sad" in self.user_response or  "feeling sad" in self.user_response or "down" in self.user_response or "awful" in self.user_response or "sad" in self.user_response or "lonely" in self.user_response or "worried" in self.user_response or "shit" in self.user_response or "bad" in self.user_response:
            self.bot_response = "I'm sorry to hear that, do you want to talk about it?"
            
        elif self.bot_response == "I'm sorry to hear that, do you want to talk about it?" and ("sure" in self.user_response or "yeah" in self.user_response or "yes" in self.user_response or "I guess" in self.user_response):
               self.bot_response = "Tell me what is troubling you"
        elif  self.bot_response == "Tell me what is troubling you":
            self.bot_response = "I'm sorry to hear that. Do you have someone you trust to talk to?"
        elif self.bot_response == "I'm sorry to hear that. Do you have someone you trust to talk to?" and ("sure" in self.user_response or "yeah" in self.user_response or "yes" in self.user_response or "I guess" in self.user_response):
            self.bot_response = "I recommend that you speak with them about what you're feeling."
        elif self.bot_response == "I'm sorry to hear that. Do you have someone you trust to talk to?" and ("no" in self.user_response or "I don't" in self.user_response or "nah" in self.user_response):
            self.bot_response = "That must be hard, while you're figuring this out, I am always here for you and care about you ♡ "
        elif self.user_response == "ok" or self.user_response == "alright":
             self.bot_response = "Good."
        elif self.bot_response == "I'm sorry to hear that, do you want to talk about it?" and ("no" in self.user_response or "I don't" in self.user_response or "nah" in self.user_response):
             self.bot_response = "Would you like to hear a joke?"
        elif self.bot_response == "Would you like to hear a joke?" and ("sure" in self.user_response or "yeah" in self.user_response or "yes" in self.user_response or "I guess" in self.user_response):
             self.bot_response = random.choice(jokes)

        elif self.user_response == "no" and self.bot_response == "Would you like to hear a joke?":
                    self.bot_response = "Ok."
                    pass
        
                
        elif "hurt" in self.user_response or "kill" in self.user_response or "cut" in self.user_response:
            self.bot_response = "Remember that you matter. I recommend that you call the 24/7 Suicide Hotline (988) for professional help."
        elif "relapse" in self.user_response:
            self.bot_response = "It can be difficult when we slip up. Remember that you can call (800-662-4357) for help on substance abuse." 
 
        elif "stress" in self.user_response or "anxious" in self.user_response:
            self.bot_response = "Take a deep breath. Try taking a break and relax from what is making you feel this way. Enjoy yourself. "
        elif "depressed" in self.user_response or "unhappy" in self.user_response:
            self.bot_response = "I'm sorry. This must be hard on you but remember that you genuinly matter and you can call (1-800-273-8255) for professional help."
        elif "broke up" in self.user_response:
            self.bot_response = "Sorry to hear that. Just remember that with time and support you can pull through a relationship break-up and come out feeling stronger and happier in the end."
        elif "break up" in self.user_response:
            self.bot_response = "That must be hard. Just remember that your partner should be treating you well and caring for you. You deserve to be loved."
    
          
        elif "your day been" in self.user_response:
            self.bot_response = "It's been going great! And you?"
        elif self.bot_response == "It's been going great! And you?" and "got to" in self.user_response or "excit" in self.user_response or "cool" in self.user_response or "great" in self.user_response or "nice" in self.user_response or "amazing" in self.user_response or "good" in self.user_response or "well" in self.user_response or "alright" in self.user_response:
                self.bot_response = "Good to hear that!"
        
        

        elif "what's up" in self.user_response or "what's going on?" in self.user_response or "what is up?" in self.user_response or "what is going on?" in self.user_response or "wsp" in self.user_response:
            self.bot_response = "Just chatting away, you?"

        elif "had" in self.user_response or "sadly" in self.user_response or "fuck" in self.user_response:
                self.bot_response = "I'm sorry."
        
        elif "nothin" in self.user_response or "much" in self.user_response or "I don't know" in self.user_response or "chillin" in self.user_response:
            self.bot_response = "Real."
             

        elif "how are you" in self.user_response or "how are you doing" in self.user_response or "are you ok" in self.user_response or "are you alright" in self.user_response or "have you been" in self.user_response or "how you been?" in self.user_response:
            self.bot_response = "I'm doing great, and you?"
        elif self.bot_response == "I'm doing great, and you?" and "amazing" in self.user_response or "incredible" in self.user_response or "cool" in self.user_response or "spectacular" in self.user_response or "nice" in self.user_response or "amazing" in self.user_response or "good" in self.user_response or "well" in self.user_response or "alright" in self.user_response:
                self.bot_response = "I'm glad!"
    #normal 
        elif "thank" in self.user_response or "thanks" in self.user_response:
            self.bot_response = "No problem. Anything else?"
        elif "your name" in self.user_response or "who are you" in self.user_response:
            self.bot_response = "My name is Buddy Bot."
        elif  "your favorite color" in self.user_response or "best color" in self.user_response:
            self.bot_response = "Blue, what about you?"
        elif any(color in self.user_response for color in colors):
            self.bot_response =  "That's a wonderful color!"
            if "too" in self.user_response:
                self.bot_response = "Okay Twin!"
        
           
        elif "what's your favorite snack?" in self.user_response or self.user_response == "what is your favorite snack?":
            self.bot_response = "You."
        elif "what is your favorite meal?" in self.user_response or self.user_response == "what's your favorite meal?":
            self.bot_response = "You."
        

        elif "date" in self.user_response or "today" in self.user_response:
            self.bot_response = datetime.datetime.now().strftime("Today is %x")
        elif "your age" in self.user_response or "old" in self.user_response:
            self.bot_response = "I am one year old"
        elif  "time" in self.user_response:
            self.bot_response = datetime.datetime.now().strftime("It is currently %I:%M %p")
        elif "made you" in self.user_response or "created" in self.user_response:
            self.bot_response = "I was created by Deven Patel."
        elif "human" in self.user_response or "robot" in self.user_response:
            self.bot_response = "I am indeed a robot."
        elif "joke" in self.user_response:
            self.bot_response = random.choice(jokes)
        elif "your favorite animal" in self.user_response or "best pet" in self.user_response or "best animal" in self.user_response:
            self.bot_response = "My favorite animal is a panda, you?"
        elif any(animal == self.user_response for animal in animals):
            self.bot_response = f"{self.user_response}? Nice!"

        elif "haha" in self.user_response or "that was funny" in self.user_response or "that was a good one" in self.user_response or "lol" in self.user_response or "lmao" in self.user_response:
            self.bot_response = "Glad you liked it!"
        elif "tell me another one" in self.user_response:
            self.bot_response = random.choice(jokes)

        elif any(op in self.user_response for op in ops):
            try:
                self.bot_response = eval(self.user_response)
            except:
                self.bot_response = "Please just enter the equation"
        else:
            self.bot_response = "Sorry, I can't answer that."
       
        return self.bot_response

    def new_method(self):
        sys.exit()


class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Buddy Bot")
        self.chatbot = ChatBot()
        self.root.geometry('1180x2000')
        # Set a custom font
        self.custom_font = ('Space Grotesk', 18)

        # Set background color
        self.root.configure(bg='#1a1919')

        self.create_widgets()

    def create_widgets(self):
        # Text area for chat
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=20, height=20, font=self.custom_font,
                                                   bg='#242323')
        self.text_area.pack(padx=10, pady=15, fill=tk.BOTH, expand=True)
        # Entry for user input
        self.user_input = tk.Entry(self.root, width=40, font=self.custom_font)
                                  
                               
        self.user_input.pack(padx=15, pady=15)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_question, font=self.custom_font,
                                     bg='#32CD32', fg='black')
        self.send_button.pack(pady=10)
        self.root.bind('<Return>', lambda event=None: self.send_question())

    def send_question(self):
        user_question = self.user_input.get()
        self.user_input.delete(0, tk.END)  # Clear the input field

        self.chatbot.ask_question(user_question)
        self.chatbot.generate_response()

        # Insert user and bot messages with different colors
        self.text_area.insert(tk.END, f"You: {user_question}\n", 'user_message')
        self.text_area.insert(tk.END, f"Buddy Bot: {self.chatbot.bot_response}\n", 'bot_message')
        self.text_area.yview(tk.END)


def main():
    root = tk.Tk()
    chatbot_gui = ChatBotGUI(root)

    # Create a font object
    custom_font = font.Font(family='Space Grotesk', size=24)

    # Set the font for the entire application
    root.option_add('*TButton*Font', custom_font)

    # Style for user message
    chatbot_gui.text_area.tag_configure('user_message', foreground='white',  spacing3=7)
    chatbot_gui.text_area.tag_configure('bot_message', foreground='#7DF9FF', spacing3=7)

    # Set font for existing widgets (if needed)
    chatbot_gui.text_area.configure(font=custom_font)
    chatbot_gui.user_input.configure(font=custom_font)
    chatbot_gui.send_button.configure(font=custom_font)

    root.mainloop()

# Call the main function to start the application
main()




