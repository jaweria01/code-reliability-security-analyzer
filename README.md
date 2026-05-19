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
