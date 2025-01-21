from pipeline_QA import ask_question

if __name__ == "__main__":
    print("Welcome to Diorite")
    while True:
        prompt = input("Ask your question, or type exit to quit: ")
        if prompt.lower() == 'exit':
            print("Goodbye")
            break
        response = ask_question(prompt)
        print(f"Answer: {response}")