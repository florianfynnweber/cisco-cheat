import pyperclip
import time
import traceback
import json
import clipboard

questions = json.load(open("questions/" +input("Question file (e.g. '2_1'): ") + ".json"))
old = ""
while True:
    try:

        question = pyperclip.paste()
        if question and not question.startswith("A: ") and question !=old:
            answers = []
            for q, a in questions:
                if question.strip() in q:
                    answers.append(a)
            old = question
            print("A: " + " //// ".join(["; ".join(a) for a in answers]))
            #clipboard.copy("A: " + " //// ".join(["; ".join(a) for a in answers]))

    except:
        # traceback.print_exc()
        pass

    finally:
        time.sleep(0.5)
