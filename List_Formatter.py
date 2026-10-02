import os
os.system("cls")

input_file = open("Formatter_input.txt","r")
output_file = open("Formatter_output.txt","w")

def if_it_has_newlines():
    output_file.write("['")
    input_text = input_file.read()
    input_text = input_text.replace("\n", "','")
    output_file.write(input_text)
    output_file.write("']")

    input_file.close
    output_file.close

def if_it_has_spaces():
    output_file.write("['")
    input_text = input_file.read()
    input_text = input_text.replace(" ", "','")
    output_file.write(input_text)
    output_file.write("']")

    input_file.close
    output_file.close

def if_it_is_a_list():
    input_text = input_file.read()
    input_text = input_text.replace("]", "")
    input_text = input_text.replace("[", "")
    input_text = input_text.replace("'", "")
    input_text = input_text.replace('"', "")
    input_text = input_text.replace(",", " ")
    output_file.write(input_text)

    input_file.close
    output_file.close

def what_to_look_for():
    newlines_or_spaces = input("Replace newlines or spaces?\n")
    
    newlines_or_spaces = newlines_or_spaces.upper()

    if newlines_or_spaces == "NEWLINES":
      if_it_has_newlines()
    elif newlines_or_spaces == "SPACES":
        if_it_has_spaces()
    else:
        print("Invalid answer, please enter 'newlines' or 'spaces'.")
        what_to_look_for()

def list_ask():
    list_question = input("Format to or from a list?\n")

    list_question = list_question.upper()

    if list_question == 'TO':
        what_to_look_for()
    elif list_question == 'FROM':
        if_it_is_a_list()
    else:
        print("Invalid answer, please enter 'to' or 'from'.")
        list_ask()

#I'm pretty forgetful and this could help
output_file.write("Remember to click, hold, and go down instead of trying to take your mouse to the end of the line :D\n\n\n")

list_ask()
