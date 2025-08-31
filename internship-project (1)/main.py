import os

def run_script(path):
    os.system(f"python {path}")

def main():
    while True:
        print("\n===== Internship Project Menu =====")
        print("1. Python Basics")
        print("2. Pandas")
        print("3. Visualization")
        print("4. Machine Learning")
        print("5. GenAI Demo")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\n-- Python Basics --")
            scripts = [
                "src/01_python_basics/variables_datatypes.py",
                "src/01_python_basics/operators.py",
                "src/01_python_basics/conditionals.py",
                "src/01_python_basics/loops.py",
                "src/01_python_basics/list_tuple_set_dict.py"
            ]
            for s in scripts:
                print(f"\nRunning {s}...")
                run_script(s)
        
        elif choice == "2":
            print("\n-- Pandas --")
            scripts = [
                "src/02_pandas/pandas_basics.py",
                "src/02_pandas/data_cleaning.py",
                "src/02_pandas/data_analysis.py"
            ]
            for s in scripts:
                print(f"\nRunning {s}...")
                run_script(s)
        
        elif choice == "3":
            print("\n-- Visualization --")
            scripts = [
                "src/03_visualization/line_chart.py",
                "src/03_visualization/bar_chart.py",
                "src/03_visualization/histogram.py",
                "src/03_visualization/scatter_plot.py"
            ]
            for s in scripts:
                print(f"\nRunning {s}...")
                run_script(s)
        
        elif choice == "4":
            print("\n-- Machine Learning --")
            scripts = [
                "src/04_machine_learning/linear_regression.py",
                "src/04_machine_learning/classification.py",
                "src/04_machine_learning/clustering.py"
            ]
            for s in scripts:
                print(f"\nRunning {s}...")
                run_script(s)
        
        elif choice == "5":
            print("\n-- GenAI Demo --")
            run_script("src/05_genai/genai_demo.py")
        
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
