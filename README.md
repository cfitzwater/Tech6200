# Tech6200
# Project is to create a functional command-line calculator that will handle user input, perform basic arithmetic, and gracefully manage common errors.

# Technologies used 
  VSCode,Gemini, Claude 4.1

# Initial AI prompts (Claude 4.1)
  The program must first prompt the user to enter a number.
  Must prompt for an arithmetic operation (+, -, *, /).
  Must prompt for a second number.
  Program must calculate and display the result in a clear, human-readable format.
  Application must not crash if the user enters non-numeric input or attempts to divide by zero. In these error cases, a friendly message should be displayed to the user.

# Run python file
  Line 1 prompted for number 
  Line 2 prompted for arithmetic symbol
  Line 3 promtped for number
  Command line appeared and no output was generated.

# Prompt presented to (Gemini extension)
  can you review my code and tell me why Im not getting an output?

# Response received from Gemini
  Your script is not producing output for addition, subtraction, or multiplication because the print statement that displays the result is inside the elif block for division. This means the result   is only printed when you perform a division operation.

  To fix this, the print statement should be moved to after the if/elif block that calculates the result.

  Would you like me to fix the code for you?

# Gemini rearranged code appropriately and calculator appears to be working including presenting error messages
  If a non numeric number is entered error message provided: "Please enter a valid number"

  If the second number of (/) = 0, error provided: "Cannot divide by zeero! Please try again with a non-zero second number."

