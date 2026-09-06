# SHA-256 Encoder

A lightweight desktop application for generating and validating SHA-256 hashes through a simple graphical interface.

## About the Project

This repository contains a local SHA-256 hashing utility built with Python and Tkinter.

The application allows users to enter plain text and instantly generate its SHA-256 hash. It also includes a validator for checking whether a manually entered value follows the standard SHA-256 format.

All processing takes place locally on the user's computer.

## Features

- Real-time SHA-256 hashing while typing.
- Support for multi-line text and line breaks.
- SHA-256 hash format validation.
- Clear input button.
- Copy hash to clipboard.
- Responsive and resizable interface.
- Rounded panels and modern dark-themed design.
- No external services or network requests.

## How It Works

### Plain Text → SHA-256 Hash

Enter any text in the left-hand field. The application automatically generates the corresponding SHA-256 hash in the right-hand field.

### SHA-256 Hash Validation

Enter a value in the right-hand field to check whether it follows the SHA-256 format.

A valid SHA-256 hash contains:

- Exactly 64 characters.
- Only hexadecimal characters (`0-9`, `a-f`).

> SHA-256 is a one-way cryptographic hashing algorithm. A hash cannot be decoded back into its original text.

## Requirements

- Python 3.x
- Tkinter

## Installation

Clone the repository:

```bash
git clone https://github.com/R4winput/SHA-256-Encoder.git
cd SHA-256-Encoder
```
> ⚠️ This project is developed for educational purposes.
> SHA-256 is a cryptographic hash function, not an encryption algorithm.
