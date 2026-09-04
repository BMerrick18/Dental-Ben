class InputService:
    
    #return a list from a comma separated input
    def comma_separated_to_list(self, user_input):
        user_input = input(user_input)
        return [
            item.strip().lower() for item in user_input.split(',') if item.strip()
        ]

    #return the answer to an input in lower case 
    def get_text(self, question):
        return input(question).strip().lower()

    #return a name with capitalised first letters from an input
    def get_name(self, question):
        return input(question).title().strip()

    #return capitalised text from an input
    def get_uppercase_text(self, question):
        return input(question).upper().strip()

    #return the answer to an input or default if no answer
    def get_with_default(self, question, default):
        answer = input(question).strip()

        if answer == "":
            return default
        
        return answer

    #return a float from an input, or default if blank; retry on invalid input
    def get_float(self, question, default=None, min_value=None, max_value=None):
        answer = input(question).strip()

        if answer == "":
            return default

        try:
            value = float(answer)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")
            return self.get_float(question, default, min_value, max_value)

        if min_value is not None and value < min_value:
            print(f"Please enter a number of at least {min_value}.")
            return self.get_float(question, default, min_value, max_value)

        if max_value is not None and value > max_value:
            print(f"Please enter a number of at most {max_value}.")
            return self.get_float(question, default, min_value, max_value)

        return value


