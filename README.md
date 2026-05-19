# Code Reliability & Security Analyzer

A Python-based static analysis tool designed to detect potential security vulnerabilities and software reliability issues using AST-driven program analysis.

## Overview

This project analyzes Python source code without executing it and identifies potentially unsafe coding patterns, security risks, and maintainability concerns. The analyzer performs static code analysis using Python's Abstract Syntax Tree (AST) module and generates structured reports with severity classifications and remediation suggestions.

The project was developed to explore concepts related to:

- Static Program Analysis
- Software Reliability
- Secure Coding Practices
- Security-Oriented Code Scanning
- Developer Tooling and CLI Engineering

---

## Features

- AST-based static code analysis
- Multi-file and directory scanning
- Security vulnerability detection
- Reliability issue detection
- Severity classification (HIGH / MEDIUM / LOW)
- Intelligent remediation suggestions
- JSON report generation
- Colorized terminal output
- Command-line interface support

---

## Currently Supported Detections

### Security Checks
- Hardcoded secrets/passwords
- Dangerous function usage (`eval`, `exec`)
- Suspicious imports (`os`, `subprocess`)

### Reliability Checks
- Unused variables
- Potential maintainability concerns

---

---

## Sample Analysis Outputs

The following screenshots demonstrate the analyzer detecting potential security vulnerabilities and software reliability issues across multiple Python files.

### Multi-file Project Analysis

The analyzer scans entire directories, detects potentially unsafe coding patterns, classifies issue severity levels, and provides remediation suggestions.

![Directory Scan Output](screenshots/directory_scan_output.png)

---

### Security and Reliability Issue Detection

Example output showing detection of dangerous functions, suspicious imports, hardcoded secrets, and unused variables.

![Security Detection Output](https://github.com/jaweria01/code-reliability-security-analyzer/blob/c164fb2068ec54cf629cee2be2a198d455b58209/screenshots/terminal-output-buggy_code.png)
![Security Detection Output](https://github.com/jaweria01/code-reliability-security-analyzer/blob/999f18a884c055ae3dd2a08bb8ab9e88cc7353a0/screenshots/terminal-output-buggy_code2.png)
![Security Detection Output](https://github.com/jaweria01/code-reliability-security-analyzer/blob/999f18a884c055ae3dd2a08bb8ab9e88cc7353a0/screenshots/terminal_output_test_code.png)

---

### Analysis Summary Dashboard

The tool generates a final analysis summary including the number of scanned files and categorized issue statistics.

![Analysis Summary](https://github.com/jaweria01/code-reliability-security-analyzer/blob/999f18a884c055ae3dd2a08bb8ab9e88cc7353a0/screenshots/summary_dashboard.png)

---

### JSON Report Generation

The analyzer exports structured machine-readable JSON reports for further processing and automation workflows.

See json file under **reports** folder


---

## Project Structure

```bash
code-reliability-security-analyzer/
│
├── analyzer/
│   └── code_analyzer.py
│
├── samples/
│   ├── buggy_code.py
│   └── test_code.py
│
├── reports/
│   └── analysis_report.json
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
