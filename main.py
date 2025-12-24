from prompt import ALL_PROMPTS
from run_experiment import run_experiment

# The main function runs the whole program
def main():
    output = run_experiment(ALL_PROMPTS)
    print("\n=== MODEL OUTPUT ===\n")
    print(output)
    
# Driver code
if __name__ == "__main__":
    main()