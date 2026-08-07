class InputService:
    
    #return a list from a comma separated input
    def comma_separated_to_list(self, user_input):
        return [
            item.strip().lower() for item in user_input.split(',') if item.strip()
        ]

    #return the answer to an input
    def get_text(self, question):
        return input(question).strip()

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


