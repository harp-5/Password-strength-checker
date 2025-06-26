# Password Strength Checker

A Python script that validates password strength against multiple criteria.

## Features
- Minimum 8 characters
- At least one uppercase letter (A-Z)
- At least one lowercase letter (a-z)
- At least one digit (0-9)

## Installation
`bash
git clone https://github.com/harp-5/Password-strength-checker.git
cd Password-strength-checker
python3 password_checker.py

## Usage 
`bash
$ python3 password_checker.py
Enter password: Hello123
Strong password!

Enter password: weak  
Weak: Needs 8+ characters

## Why It's Valuable
Demonstrates core security concepts
Clean, maintainable code structure
Easy to extend with new rules

## How to Test
Try these test cases:
1. "Password123" (should pass)
2. "nocaps123" (should fail)
3. "Short1" (should fail)
