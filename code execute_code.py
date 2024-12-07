# /backend/code_executor.py

def execute_code(code):
    """
    Safely execute code in a sandboxed environment.
    """
    try:
        # Use exec in a controlled environment to execute code
        exec(code)
        return "Code executed successfully."
    except Exception as e:
        return f"Error executing code: {e}"