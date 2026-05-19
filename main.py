import ast
import json
import sys
import os
from colorama import Fore, Style, init

from analyzer.code_analyzer import CodeAnalyzer
init(autoreset=True)


# Check if file path is provided
if len(sys.argv) < 2:

    print("Usage: python main.py <python_file>")
    sys.exit()

file_path = sys.argv[1]

all_issues = []
high_count = 0
medium_count = 0
low_count = 0

# Check if input is a directory
if os.path.isdir(file_path):

    python_files = []

    # Walk through all files
    for root, dirs, files in os.walk(file_path):

        for file in files:

            if file.endswith(".py"):

                python_files.append(os.path.join(root, file))

else:
    python_files = [file_path]


# Analyze each Python file
for py_file in python_files:

    print(f"\nAnalyzing: {py_file}")

    try:

        with open(py_file, "r") as file:
            code = file.read()

        tree = ast.parse(code)

        analyzer = CodeAnalyzer()
        analyzer.visit(tree)

        # Detect unused variables
        for var_name, line in analyzer.variables:

            if var_name not in analyzer.used_variables:

                analyzer.issues.append({
                    "type": "Unused Variable",
                    "severity": "LOW",
                    "line": line,
                    "message": f"The variable '{var_name}' is assigned but never used.",
                    "suggestion": "Remove unused variables to improve code readability and maintainability."
                })

        # Print issues
        if analyzer.issues:

            print("\nIssues Detected:\n")

            for issue in analyzer.issues:

                severity = issue["severity"]
                if severity == "HIGH":
                    high_count += 1

                elif severity == "MEDIUM":
                    medium_count += 1

                else:
                    low_count += 1

                if severity == "HIGH":
                    color = Fore.RED

                elif severity == "MEDIUM":
                    color = Fore.YELLOW

                else:
                    color = Fore.GREEN

                print(color + f"[{severity}] {issue['type']}" + Style.RESET_ALL)

                print(f"Line       : {issue['line']}")
                print(f"Explanation: {issue['message']}")
                print(f"Suggestion : {issue['suggestion']}")

                print("-" * 40)

        else:
            print("No issues detected.")

        # Save issues
        # Add filename to each issue
        for issue in analyzer.issues:

            issue["file"] = py_file

            all_issues.append(issue)
        
    except SyntaxError as e:

        print(Fore.RED + "Syntax Error Detected!" + Style.RESET_ALL)

        print(f"File   : {py_file}")
        print(f"Line   : {e.lineno}")
        print(f"Message: {e.msg}")


# Save combined JSON report
with open("reports/analysis_report.json", "w") as report_file:

    json.dump(all_issues, report_file, indent=4)

print("\nCombined JSON report generated successfully.")
print("\nAnalysis Summary")
print("-" * 30)

print(f"Files Scanned : {len(python_files)}")
print(f"HIGH Issues   : {high_count}")
print(f"MEDIUM Issues : {medium_count}")
print(f"LOW Issues    : {low_count}")