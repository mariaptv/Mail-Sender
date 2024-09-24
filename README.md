### Mail Sender Automation

This Python script automates the process of creating personalized letters for a list of invitees. It reads a template letter, replaces a placeholder with actual names from a list, and saves the personalized letters in a designated output folder.

### Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)

### Overview

The script performs the following tasks:

1. **Reads Names**: Loads a list of invitee names from `invited_names.txt`.
2. **Reads Template**: Loads a letter template from `starting_letter.txt`, which contains a placeholder `[name]`.
3. **Generates Letters**: Replaces the `[name]` placeholder with each invitee's name.
4. **Saves Letters**: Writes the personalized letters to the `ReadyToSend` folder.

### Features

- **Automated Personalization**: Quickly generates personalized letters for each invitee.
- **Easy Configuration**: Simple file-based input and output makes customization straightforward.
- **Scalable**: Handles any number of invitees efficiently.

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
