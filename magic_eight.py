def add_question():
    x = input("what is your question?:")
    return x

def get_answer():
    answer_list =  ["It is certain.", "It is decidedly so.", "Without a doubt.","Yes - definitely."\
                    "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good."\
                    "Yes.","Signs point to yes.","Reply hazy, try again","Ask again later.",\
                    "Better not tell you now.", "Cannot predict now.","Concentrate and ask again."\
                    "Don't count on it.", "My reply is no.", "My sources say no","Outlook not so good."\
                    "Very doubtful."]
    import random
    i = random.randint(0,20)
    return answer_list[i]
