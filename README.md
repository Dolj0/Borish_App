# Borish_App
 Submission For HackNotts  2021

 This is an app for spoofing the current UK prime minister, Boris Johnson, that attempts to predict his continuation given an input, the text is then displayed and read using text to speech.
 
 We scraped ~1,500,000 characters from the gov.uk website using the beautiful soup package and then fed this data into a recurrent neural network created using tensorflow in python. The RNN was adapted from --> https://www.tensorflow.org/text/tutorials/text_generation
 
 We then saved this RNN and put it into a tkinter GUI which allows a user to enter in a prompt for our Boris bot to finish. The text is also then read out by a simple text to speech package.
 
 With more time, a more realistic and bespoke TTS would be trained using Boris's real voice. The RNN would also be improved upon as it rarely produces coherent text.
 
 
 
 
 
