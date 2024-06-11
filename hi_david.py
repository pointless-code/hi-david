import time
import sys

def typing_effect(text):
    try:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
    except KeyboardInterrupt:
        print("\nExiting gracefully... Bye David!")
        sys.exit(0)

def main():
    try:
        typing_effect("Let me think.... Is it David?")
        response = input("\nType 1 for Yes and 2 for No: ")

        if response == "1":
            typing_effect("\nI knew it. Hi David!")
        elif response == "2":
            percentage = 100
            while True:
                typing_effect(f"\nAre you sure {percentage}% it's not David?")
                response = input("\nType 1 for Yes and 2 for No: ")
                if response == "1":
                    percentage += 10
                elif response == "2":
                    typing_effect("\nI knew it. Hi David!")
                    break
    except KeyboardInterrupt:
        print("\nExiting gracefully... Bye David!")

if __name__ == "__main__":
    main()