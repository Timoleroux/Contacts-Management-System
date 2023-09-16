<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>mini-projet-dictionnaire
</h1>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
</p>
<img src="https://img.shields.io/github/languages/top/mini-projet-dictionnaire?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/mini-projet-dictionnaire?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/mini-projet-dictionnaire?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/mini-projet-dictionnaire?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#️-features)
- [📂 Project Structure](#-project-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✔️ Prerequisites](#️-prerequisites)
  - [📦 Installation](#-installation)
  - [🎮 Using mini-projet-dictionnaire](#-using-mini-projet-dictionnaire)
  - [🧪 Running Tests](#-running-tests)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The core functionality of this project is to provide a directory management tool, allowing the user to add, search, display, and copy phone numbers stored in a JSON file. It aims to simplify and streamline the process of managing and accessing contact information. By providing an intuitive user interface and automation features, this project offers convenience and efficiency for users in managing their contact directory.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| ⚙️ Architecture     | The codebase follows a modular and object-oriented design pattern, separating the directory management tool, JSON database generator, and contact directory application into different components. Each component has distinct responsibilities and can be easily maintained or extended. |
| 📖 Documentation   | The codebase has comprehensive documentation that provides explanations of each file's purpose, functional descriptions of the core functionalities, and usage examples. The documentation allows developers to easily understand and contribute to the project. |
| 🔗 Dependencies    | The system relies on PySide6 for developing the contact directory application's user interface and PrettyTable for formatting tables in the directory management tool. Pyperclip is used for copying phone numbers to the clipboard. |
| 🧩 Modularity      | The codebase demonstrates good modularity by separating concerns into different files and functions. This allows for easier code maintenance, debugging, and reusability of components. Components like loading/writing JSON files, formatting dictionaries, and converting phone numbers are reusable across different parts of the application. |
| ✔️ Testing          | The testing strategies and tools used in the codebase are not specified in the provided information. It is recommended to investigate the repository for any existing testing frameworks or manually implemented tests to evaluate the testing approach comprehensiveness. |
| ⚡️ Performance      | Given the provided information only, there isn't enough information to specifically analyze the system's performance in terms of speed, efficiency, and resource usage. It is advisable to identify if any potential bottlenecks or performance-critical areas exist and assess them directly. |
| 🔐 Security        | The provided information does not explicitly mention any security measures used by the system. It would be necessary to examine the actual source code and data handling procedures to evaluate the security measures employed by the application. |
| 🔀 Version Control | The codebase utilizes Git for version control. Git enables efficient collaboration and tracking of changes across the project's different files. Branching and merging capabilities can be used to manage feature development and ensure code integrity. |
| 🔌 Integrations    | The system does not seem to have any specific mentioned integrations with external systems or services in the provided information. However, given the modularity and flexibility of the project structure, it can be extended to integrate with other systems easily. |
| 📶 Scalability     | The provided information does not provide insight into how the system handles growth. It would be beneficial to assess the codebase's scalability considering factors such as database performance, concurrent access, and code optimization as the size of the directory or the number of users increases. |

---


## 📂 Project Structure




---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [console_app.py](https://github.com/mini-projet-dictionnaire/blob/main/console_app.py)    | This code is a directory management tool. It allows the user to add, search, display, and copy phone numbers stored in a JSON file. It uses PrettyTable for table formatting and Pyperclip for copying phone numbers to the clipboard. The core functionalities include adding entries to the directory, searching for entries by name or phone number, displaying the directory contents, and copying phone numbers to the clipboard. |
| [generator.py](https://github.com/mini-projet-dictionnaire/blob/main/apps\generator.py)   | The code generates a JSON database file with random names and phone numbers. It prompts for confirmation to delete the existing content and then generates and updates the database with the specified number of items.                                                                                                                                                                                                                |
| [main.py](https://github.com/mini-projet-dictionnaire/blob/main/apps\main.py)             | This code creates a contact directory application using PySide6. It allows users to search, add, delete, and copy phone numbers. The application loads data from a JSON database and updates the user interface accordingly.                                                                                                                                                                                                           |
| [ressources.py](https://github.com/mini-projet-dictionnaire/blob/main/apps\ressources.py) | This code provides functionalities for loading and writing JSON files, formatting dictionaries, and converting phone numbers between French and international formats.                                                                                                                                                                                                                                                                 |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 📦 Installation

1. Clone the mini-projet-dictionnaire repository:
```sh
git clone C:/Users/timol/Documents/GitHub/mini-projet-dictionnaire
```

2. Change to the project directory:
```sh
cd mini-projet-dictionnaire
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using mini-projet-dictionnaire

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
