from pipeline_QA import ask_question

if __name__ == "__main__":
    print("Welcome to Diorite")
    context = input("Enter a question: ")

    while True:
        question = input("\Ask Question:")
        if question.lower() == 'exit':
            print("Goodbye")
            break
        answer = ask_question(question, context)
        print(f"Answer: {answer}")


