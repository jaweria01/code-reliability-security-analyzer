import ast
class CodeAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.variables = []
        self.used_variables = []
        self.issues = []

    # Detect variable assignments
    # Detect hardcoded passwords
    def visit_Assign(self, node):

        for target in node.targets:

            if isinstance(target, ast.Name):

                variable_name = target.id

                self.variables.append((variable_name, node.lineno))

                # Detect suspicious password assignment
                if "password" in variable_name.lower():

                    if isinstance(node.value, ast.Constant):

                        self.issues.append({
                            "type": "Hardcoded Secret",
                            "severity": "HIGH",
                            "line": node.lineno,
                            "message": "Possible hardcoded password detected.",
                            "suggestion": "Use environment variables or secret managers instead of hardcoding credentials."
                        })

        self.generic_visit(node)
    #


    # Detect variable usage
    def visit_Name(self, node):

    # Only count variables that are READ/USED
        if isinstance(node.ctx, ast.Load):
            self.used_variables.append(node.id)

        self.generic_visit(node)


    # Detect dangerous functions like eval()
    # Detect dangerous exec()
    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):

            if node.func.id == "eval":
                self.issues.append({
                    "type": "Dangerous Function",
                    "severity": "HIGH",
                    "line": node.lineno,
                    "message": "Use of eval() can be dangerous.",
                    "suggestion": "Avoid eval(). Consider safer parsing or validation methods."
                })

            if node.func.id == "exec":
                self.issues.append({
                    "type": "Dangerous Function",
                    "severity": "HIGH",
                    "line": node.lineno,
                    "message": "Use of exec() can be dangerous.",
                    "suggestion": "Avoid exec() unless absolutely necessary."
                })
        self.generic_visit(node)
        # Detect suspicious imports
    def visit_Import(self, node):

        suspicious_modules = ["os", "subprocess"]

        for alias in node.names:

            if alias.name in suspicious_modules:

                self.issues.append({
                    "type": "Suspicious Import",
                    "severity": "MEDIUM",
                    "line": node.lineno,
                    "message": f"Importing '{alias.name}' may require security review.",
                    "suggestion": "Review whether this module is necessary and ensure safe usage."
                })

        self.generic_visit(node)


    #
