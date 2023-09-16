# Contacts Manager

Vous ne parlez pas anglais ? La traduction en français se trouve [ici](#système-de-gestion-de-contacts).

This repository contains a set of Python scripts for managing a directory of contacts. These scripts provide various functionalities for adding, searching, displaying, and copying contact information. The directory is stored as a JSON file, and you can interact with it using both a graphical user interface (GUI) application and a console-based application.

## 🖥️ Scripts

### `main.py`

- This script creates a GUI application for managing contacts. It allows you to search for contacts, view contact details, copy phone numbers, add new contacts, and delete existing contacts.

### `consoleApp.py`

- This script offers a console-based interface for managing contacts. You can perform actions such as adding contacts, searching for contacts, displaying the entire directory, and copying phone numbers.

### `generator.py`

- Use this script to generate random contact data for testing purposes. It populates the contact directory with random names and phone numbers, allowing you to test the functionality of the other scripts.

### `utils.py`

- This module contains utility functions used by the other scripts, including functions for loading and saving contact data, formatting phone numbers, and more.

### `/data/repertoire.json`

- This JSON file represents the contact directory and contains sample contact data. You can replace this file with your own data or use it as a starting point for managing your contacts.

## 🏁 Getting Started

To use these scripts, follow these steps:

1. Ensure you have Python (at least v.3.8) installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. Install the required Python packages by running the following command in your terminal:

   ```bash
   pip install -r requirements.txt
   ```

3. Clone or download this repository to your local machine.

4. Run the scripts based on your preference:

   - If you prefer a graphical interface, run `main.py` to open the GUI application.

   - If you prefer a console-based interface, run `consoleApp.py` to interact with the contacts using text commands.

   - You can also use `generator.py` to populate the contact directory with random data.

## ⚠️ Important Notes

Ensure that the contact data is stored in the `/data/repertoire.json` file. You can replace this file with your own data or modify its contents as needed in `utils.py`.

## 🤝 Contributing

Contributions to this project are welcome! If you have any improvements or feature suggestions, feel free to fork the repository and submit a pull request.

---

# Gestionnaire de Contacts

You don't speak french? English translation [here](#contacts-management-system).

Ce projet contient un ensemble de scripts Python pour la gestion d'un répertoire de contacts. Ces scripts offrent diverses fonctionnalités pour ajouter, rechercher, afficher et copier des informations de contact. Le répertoire est stocké sous forme d'un fichier JSON, et vous pouvez interagir avec à l'aide d'une application avec interface graphique (GUI) et d'une application en mode console.

## 🖥️ Scripts

### `main.py`

- Ce script crée une application GUI pour la gestion des contacts. Il vous permet de rechercher des contacts, d'en voir les détails, de copier des numéros de téléphone, d'ajouter de nouveaux contacts et d'en supprimer.

### `consoleApp.py`

- Ce script offre une interface en mode console pour la gestion des contacts. Vous pouvez effectuer des actions telles que l'ajout de contacts, la recherche de contacts, l'affichage de l'ensemble du répertoire et la copie de numéros de téléphone.

### `generator.py`

- Utilisez ce script pour générer des données de contact aléatoires à des fins de test. Il remplit le répertoire de contacts avec des noms et des numéros de téléphone aléatoires, vous permettant ainsi de tester la fonctionnalité des autres scripts.

### `utils.py`

- Ce module contient des fonctions utilitaires utilisées par les autres scripts, notamment des fonctions pour charger et sauvegarder des données de contact, formater des numéros de téléphone, et plus encore.

### `/data/repertoire.json`

- Ce fichier JSON représente le répertoire de contacts et contient des données de contact d'exemple. Vous pouvez remplacer ce fichier par vos propres données ou l'utiliser comme point de départ pour la gestion de vos contacts.

## 🏁 Mise en route

Pour utiliser ces scripts, suivez ces étapes :

1. Assurez-vous d'avoir Python (au moins la version 3.8) installée sur votre système. Vous pouvez le télécharger depuis [le site officiel de Python](https://www.python.org/downloads/).

2. Installez les packages Python requis en exécutant la commande suivante dans votre terminal :

   ```bash
   pip install -r requirements.txt
   ```

3. Clonez ou téléchargez ce dépôt sur votre machine.

4. Exécutez les scripts en fonction de vos préférences :

   - Si vous préférez une interface graphique, exécutez `main.py` pour ouvrir l'application GUI.

   - Si vous préférez une interface en mode console, exécutez `consoleApp.py` pour interagir avec les contacts à l'aide de commandes texte.

   - Vous pouvez également utiliser `generator.py` pour remplir le répertoire de contacts avec des données aléatoires.

## ⚠️ Notes Importantes

Assurez-vous que les données de contact sont stockées dans le fichier `/data/repertoire.json`. Vous pouvez remplacer ce fichier par vos propres données ou modifier son contenu selon vos besoins dans `utils.py`.

## 🤝 Contribution

Les contributions à ce projet sont les bienvenues ! Si vous avez des améliorations ou des suggestions de fonctionnalités, n'hésitez pas à créer une branche du dépôt (fork) et à soumettre une demande de fusion (pull request).
