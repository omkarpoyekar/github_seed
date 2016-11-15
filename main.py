#!/usr/bin/env python3
"""
Simple Hello World example for the GitHub Seed project.
This demonstrates basic Python functionality.
"""

def greet(name="World"):
    """
    Greet someone with a friendly message.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"

def main():
    """Main function to run the greeting example."""
    print(greet())
    print(greet("GitHub"))
    print("Welcome to your seed project!")

if __name__ == "__main__":
    main()
