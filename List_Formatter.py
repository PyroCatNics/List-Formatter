import os
os.system("cls")

input_file = open("c:\\Users\\jacko\\Python Projects\\Formatting\\Formatter_input.txt","r")
output_file = open("c:\\Users\\jacko\\Python Projects\\Formatting\\Formatter_output.txt","w")

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



output_file.write("Remember to click, hold, and go down instead of trying to take your mouse to the end of the line :D\n\n\n")

if_it_has_newlines()