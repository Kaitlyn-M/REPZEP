# Imports the Wikipedia API, which the AI uses to research information
import wikipedia
# Imports playsound, which allows the AI to vocally speak
import playsound
# Imports pyttsx3, which allows Python to convert text to speech
import pyttsx3
# Imports speech recognition, which helps recognize speech to convert into text
import speech_recognition as sr

# Introduces the AI Assistant Program
def intro():
    
    # Introduces the AI Assistant title
    print("\n\n\t\t -=- REP-ZEP: AI Assistant -=- \n")
    # Prints out a line and creates a new line for a better UX
    print("_" * 150, "\n")
    
    # Introduces the robot's name, what the user can do, and what the robot does
    print("\n\tHello, I'm your REP (Research, Essay, Present) robot named Zep! You can ask me to research any topic you want.")
    print("\n\tIf you want, I can use the information to write an essay then vocally present it!")

# Preps the research by asking general and specific topics
def research_prep():
    
    # Asks if the user wants to use their voice or not
    use_voice = input("\n\n\tWould you like to use your voice for choosing topics? Type 'yes' or 'no': ")

    # Executes if the user wants to use their voice
    if use_voice == "yes" or use_voice == "y":
        
        # Initializes speech recognizer (recognizes user audio input)
        r = sr.Recognizer()
        
        # Initializes the microphone as the audio source
        with sr.Microphone() as source:
            
            # Asks the user what general topic Zep should research
            user_topic = print("\n\n\tAnswer with Voice: What general topic would you like me to research? ")
            # AI listens to the source and saves it in speech variable
            speech1 = r.listen(source)
            # Converts speech to text (user topic)
            user_topic = r.recognize_google(speech1)
            # Displays the user's response
            print("\n\n\tYour general essay is about: " + user_topic)

            # Prints out a line and creates a new line for a better UX
            print("_" * 150, "\n")

            # Shows that robot is researching user's topic
            print("\n\n\t\t -=- Researching topic possibilities for: " + user_topic + " -=-")
            # Variable that hold's the robot's possible research topics based on given information
            possible_topics = wikipedia.search(user_topic)
            # Introduces possible research topics based on given word or phrase
            print("\n\n\tBased on your topic, choose one of the following:")
            # Lists possible research topics based on given word or phrase
            print("\t" + str(possible_topics))

            # Asks the user what topic Zep should specifically research
            user_specific_topic = print("\n\n\tAnswer with Voice: What is your specific research topic? ")
            # AI listens to the source and saves it in speech2 variable
            speech2 = r.listen(source)
            # Converts speech to text (user's specific topic)
            user_specific_topic = r.recognize_google(speech2)
            # Displays the user's response
            print("\n\n\tYour specific essay is about: " + user_specific_topic)

    # Excecutes if the user does not what to use their voice
    else:
        
        # Asks the user what topic Zep should research
        # The user can enter their desired research topic
        user_topic = input("\n\n\tWhat general topic would you like me to research? ")

        # Prints out a line and creates a new line for a better UX
        print("_" * 150, "\n")

        # Shows that robot is researching user's topic
        print("\n\n\t\t -=- Researching topic possibilities for: " + user_topic + " -=-")
        # Variable that hold's the robot's possible research topics based on given information
        possible_topics = wikipedia.search(user_topic)
        # Introduces possible research topics based on given word or phrase
        print("\n\n\tBased on your topic, choose one of the following:")
        # Lists possible research topics based on given word or phrase
        print("\t" + str(possible_topics))

        # Asks the user what topic Zep should specifically research
        # The user can enter their specific research topic
        user_specific_topic = input("\n\tWhat is your specific research topic? ")

    # Prints out a line and creates a new line for a better UX
    print("_" * 150, "\n")

    # Introduces research on the user's topic
    print("\n\n\t\t -=- Here's some research about " + user_specific_topic + "! -=-\n")
    # Prints out a line and creates a new line for a better UX
    print("_" * 150, "\n")
    
    # Returns the user's specific topic to main()
    return user_specific_topic

# AI researches the user's specific topic
def research(user_specific_topic):
    
    # Research results are based on the user's specific research topic
    research_results = wikipedia.page(user_specific_topic)

    # Introduces the research summary
    print("\n\n\t\t -=- My Research Summary -=-\n")
    # Displays the research summary to the screen
    print(research_results.summary)
    # Prints out a line and creates a new line for a better UX
    print("_" * 150, "\n")

    # Introduces references
    print("\n\n\t\t -=- References -=-\n")
    # For each reference in the list of research results references
    # Prints out each reference on a new line
    for reference in research_results.references:
        #Prints out each reference
        print(reference)

    # Prints out a line and creates a new line for a better UX
    print("_" * 150, "\n")

    # Returns research results to main()
    return research_results

# AI writes an essay based on research results
def write_essay(research_results):
    
    # Indicates that the essay is being written
    print("\n\n\t\tWriting your essay inside 'research_essay.txt'\n")

    # Create research essay file
    file_spec = "research_essay.txt"

    # Open the research essay's file handle to append
    my_file_handle = open(file_spec, "a")

    # Writes the research summary introduction to the file
    my_file_handle.write("\n\n\t\t -=- My Research Summary -=-\n\n")
    # Converts the research results summary into a string
    # Writes the research summary to the file
    my_file_handle.write(str(research_results.summary))
 
    # Introduces the references
    my_file_handle.write("\n\n\t\t -=- References -=-\n\n")
    # For each reference in the list of research results references
    # Prints out each reference on a new line
    for reference in research_results.references:
        
        #Writes out each reference to the file
        my_file_handle.write("\n" + reference)

    # Closes the file handle so the user can not edit the file
    my_file_handle.close
   
# AI presents the essay based on research results
def present_essay(research_results):
    
    # Initilizes the text-to-speech converter
    converter = pyttsx3.init()

    # Sets the voice's speaking rate property
    converter.setProperty('rate', 150)
    # Sets the voice's volume property
    converter.setProperty('volume', 1)

    # Prints out a line and creates a new line for a better UX
    print("_" * 150, "\n")
    
    # Indicates that the essay will be presented
    print("\n\t\tI will now present the essay...\n")
    # Introduces the research summary essay
    print("\n\t\t -=- My Essay (Summary) -=-\n")
   
    # Displays the essay (summary) to the screen
    print(research_results.summary)
    
    # Research results summary text is converted into speech
    converter.say(research_results.summary)
    
    # Program waits until all speech has been said
    converter.runAndWait()

    # Indicates presentation is finished
    print("\n\n\t\tI finished presenting!\n")

# AI conducts extended essay research
def extended_research(user_specific_topic):
    
    # Research results are based on the user's specific research topic
    research_results = wikipedia.page(user_specific_topic)

    # Introduces the extended essay
    print("\n\n\t\t -=- My Extended Research -=-\n")
    # Displays the extended essay to the screen
    print(research_results.content)
    # Prints out a line and creates a new line for a better UX
    print("_" * 150, "\n")

    # For each reference in the list of research results references
    # Prints out each reference on a new line
    for reference in research_results.references:
        #Prints out each reference
        print(reference)

    # Prints out a line and creates a new line for a better UX
    print("_" * 150, "\n")

    # Returns research results to main()
    return research_results

# AI writes the extended essay based on research results
def write_essay_extended(research_results):
    
    # Indicates that the essay is being written
    print("\n\n\t\tWriting your extended essay inside 'research_extended_essay.txt'\n")

    # Create research essay file
    file_spec = "research_extended_essay.txt"

    # Open the research essay's file handle to append
    my_file_handle = open(file_spec, "a")

    # Writes the extended research introduction to the file
    my_file_handle.write("\n\n\t\t -=- My Extended Research -=-\n\n")
    # Converts the extended research essay into a string
    # Writes the extended research essay to the file
    my_file_handle.write(str(research_results.content))
 
    # For each reference in the list of research results references
    # Prints out each reference on a new line
    for reference in research_results.references:
        
        #Writes out each reference to the file
        my_file_handle.write("\n" + reference)

    # Closes the file handle so the user can not edit the file
    my_file_handle.close

# AI presents the extended essay based on research results
def present_essay_extended(research_results):
    
    # Initilizes the text-to-speech converter
    converter = pyttsx3.init()

    # Sets the voice's speaking rate property
    converter.setProperty('rate', 150)
    # Sets the voice's volume property
    converter.setProperty('volume', 1)

    # Prints out a line and creates a new line for a better UX
    print("_" * 150, "\n")
    
    # Indicates that the essay will be presented
    print("\n\t\tI will now present the extended essay...")

    # Tells the user to scroll up for extended essay content
    print("\n\t\tScroll up until you find the extended essay to follow along.")

    # Extended research results text is converted into speech
    converter.say(research_results.content)
    
    # Program waits until all speech has been said
    converter.runAndWait()

    # Indicates presentation is finished
    print("\n\n\t\tI finished presenting!\n")

# Program driver function (Every other function is executed by this one)
def main():

    # Introduces the user to the program
    intro()

    # The user's specific topic is based on the topic chosen in research prep
    user_specific_topic = research_prep()

    # Zep conducts research based on the user's specific topic
    research_results = research(user_specific_topic)

    # Asks the user if Zep should create and vocally present the summary essay
    essay_and_present = input("\n\t\tShould I create an essay and vocally present it? Type 'yes' or 'no' ")

    # Executes if the user chooses "yes" or "y"
    if essay_and_present == "yes" or essay_and_present == "y":
        
        # Zep writes the research essay based on the research results
        write_essay(research_results)

        # Zep presents the research essay
        present_essay(research_results)
    
    # Executes if the user does not choose "yes" or "y"
    else:
        
        # Indicates the program's end
        print("\n\n\t\t -=- Goodbye! Hope my research has helped you! -=-\n")

        # Forces the program to stop executing
        exit()

    # Asks the user if Zep should create and vocally present the extended essay
    will_rep = input("\n\t\tShould I research, write, and present an extended essay? Type 'yes' or 'no' ")

    # Executes if the user chooses "yes" or "y"
    if will_rep == "yes" or will_rep == "y":
        
        # Warns the user that the extended essay will take longer to present
        print("\n\t\tWARNING: The extended essay will take significantly longer to present")

        # Zep conducts extended essay research
        extended_research(user_specific_topic)

        # Zep writes the extended essay based on the research results
        write_essay_extended(research_results)

        # Zep presents the extended essay based on the research results
        present_essay_extended(research_results)
    
    # Executes if the user does not choose "yes" or "y"
    else:
        
        # Indicates the program's end
        print("\n\n\t\t -=- Goodbye! Hope my research has helped you! -=-\n")

#If there is a main function, then execute it
if __name__ == "__main__":
    # Executes the program driver (main function)
    main()