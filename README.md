# 📂 File Organizer – Script Python d’automatisation

## 🚀 Description
Ce projet est mon **premier script d’automatisation en Python**.  
L’objectif : parcourir un dossier et **organiser automatiquement les fichiers** selon leur extension (PDF, images, texte, code Python, etc.).  

Le script classe les fichiers dans des sous-dossiers (`pdf_files`, `image_files`, `text_files`, etc.) et supprime les dossiers devenus vides après le déplacement.

C’est une étape importante dans mon apprentissage de Python, car ce script m’a permis de travailler sur la **gestion des fichiers et dossiers** ainsi que la **structuration d’un programme automatisé**.

---

## 🛠️ Fonctionnalités
- 🔎 Parcours d’un dossier et de ses sous-dossiers.
- 📂 Organisation automatique des fichiers par extension.
- ✨ Création des sous-dossiers si nécessaire.
- 🔄 Déplacement des fichiers avec conservation du nom original.
- 🧹 Suppression des dossiers vides.
- ⚡ Extensible : ajoutez facilement d’autres extensions dans le dictionnaire `EXTENSIONS`.

---

## 📖 Ce que j’ai appris
- Utiliser `pathlib` pour manipuler les chemins de fichiers.
- Manipuler des fichiers et dossiers avec `shutil`.
- Structurer un script Python avec des fonctions claires.
- Gérer les erreurs et vérifier l’existence d’un chemin.
- Approfondir ma compréhension de la logique **boucles / conditions**.

---

## ▶️ Utilisation
1. Clonez ce dépôt :  
   ```bash
   git clone https://github.com/TON-PSEUDO/nom-du-repo.git
   cd nom-du-repo
2. Lancez le script avec python en précisant le chemin du dossier à organiser
  ```bash 
   python file_organisation.py [chemin_du_dossier]
````

##📌 Exemple avant / après

```
📂 Documents
   ├── rapport.pdf
   ├── image1.jpg
   ├── notes.txt
   ├── script.py

📂 Documents
   ├── pdf_files
   │    └── rapport.pdf
   ├── image_files
   │    └── image1.jpg
   ├── text_files
   │    └── notes.txt
   ├── python_files
   │    └── script.py

```

## 🤝 Contribution
Je suis encore un apprenant 🚀.

Si vous avez des suggestions, conseils ou idées d’amélioration, je serais ravi d’échanger avec vous !

👉 Retrouvez-moi aussi sur LinkedIn : www.linkedin.com/in/diallo-tsiba-souleymane-deo-gracias-07b32b380
