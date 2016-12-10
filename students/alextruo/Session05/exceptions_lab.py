#exceptions lab

#create a wrapper function that returns none rather than raising an exeption

#define the function name here and a variable for the input
def safe_input(user_input):
    #with the try clause, take the user input and assign it the variable, answer
    try:
        answer = input(user_input)
        #return whatever they entered
        return  answer
        #if it's an error, run this clause
    except (EOFError, KeyboardInterrupt, ValueError):
        #print this statement
        print("Sorry, you input an error or something.")
        #return nothing instead
        return None

if __name__ == "__main__":
    answer = safe_input("Type your text here, please: ")
    if answer is None:
        print("Okay, you did nothing and that's okay.")
    else:
        print("Your input was:", answer)

