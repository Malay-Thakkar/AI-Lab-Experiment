print("Malay Thakkar(20012011169)")
question = {"how are you": "fine",
            "name of your college": "uvpce",
            "which type of course available": "btech,bsc,bba,etc",
            "fees in btech": "57000",
            "how many semester in btech": "8",
            "fees in bsc": "25000",
            "how many semester in bsc": "6",
            "how many department in btech": "ce,it,mechanical,etc",
            "is it good college": "yes",
            "what is university name": "guni",
            "is bsc available": "yes",
            "is bba available": "yes",
            "is bpharm available": "no",
            "what is bpharm fees": "40000",
            "which is last date for admission": "30 june",
            "how far from ahmedabad": "60km",
            "is ce good": "yes depend on interest",
            "is ce hard": "depend on interest",
            "course duration of btech": "4 years",
            "course duration of bsc": "3 years",
            }


def chatbot():
    while True:
        qs = input("Enter Question: ").lower()
        symbols = {'?','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-'}
        message = ""
        for i in qs:
            if i not in symbols:
                message = message+i
        if message in ["quit",'bye']:
            print("College-bot: Bye-bye")
            break;
        elif message in question:
            print("College-bot: "+question[message])
        else:
            print("College-bot: Sorry I donot know")
chatbot()
