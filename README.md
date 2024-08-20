# poem-generation



## Architecture du repo
Le repo a deux dossiers principaux : application et finetuning.
Le dossier finetuning est composé de quatres dossiers :
 - dataset : contient tout le dataset en format .zip ainsi que les .json utilisés pour le fine-tuning
 - fine-tuning : contient les fichiers .ipynb créés pour le fine-tuning
 - chains-evaluation : contient les fichiers .ipynb créés pour tester les chaînes de LLM et évaluer les sorties du modèle fine-tuned
 - models : contient les deux dossiers avec les modèles fine-tuned

Le dossier application est composé de deux dossiers:
 - front : contient les fichiers .html, .css et .js pour la partie graphique de l'application
 - back : contient le fichier .py qui permet de faire tourner l'application ainsi qu'un ficher .ipynb pour tester l'application


## Rapport de projet

Le rapport de projet est disponible en format PDF à la racine du projet GitLab


## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README


## Name
Génération de poèmes 

## Description
Ce projet est un projet de fin de formation LLM Ops avec Datascientest. 
Il porte sur la génération de poèmes à partir d'un thème en anglais. 

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals


## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Authors 
Emeline Caruana

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
