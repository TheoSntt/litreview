
# MVP APPLICATION WEB LITREVIEW


## Avertissements

Ce repo contient une version MVP de l'application Web LITReview. 
Afin de la rendre plus facilement testable, le repository contient la base de données, la Secret Key Django, ainsi que des informations de connexions. Ces éléments devront être modifiés avant le déploiement.

## Mise en place et exécution en local de l'application

1. Téléchargez le projet depuis Github. Soit directement (format zip), soit en clonant le projet en utilisant la commande suivante dans Git Bash :  
```
git clone https://github.com/TheoSntt/OC_Project_9
```
2. Créez un environnement virtuel Python en exécutant la commande suivantes dans le Terminal de votre choix :
```
python -m venv env (env étant le nom de l'environnement, vous pouvez le changer)
```
Puis, toujours dans le terminal, activez votre environnement avec la commande suivante si vous êtes sous Linux :
```
source env/bin/activate
```
Ou bien celle-ci si vous êtes sous Windows
```
env/Scripts/activate.bat
```
3. Dans vorte environnement virtuel, téléchargez les packages Python nécessaires à la bonne exécution de l'application à l'aide de la commande suivante :
```
pip install -r requirements.txt
```
NB : Puisque la BDD contenant du contenu visant à démontrer la fonctionnalité de l'application est incluse dans le répo. Il n'est pas nécessaire de procéder aux migrations. Si vous souhaitez recréer la BDD de zéro, supprimer le fichier db.sqlite3 et procédez aux migrations, à l'aide de la commande suivante :
```		
python manage.py migrate
```
4. Vous pouvez maintenant exécuter l'application en local. Il vous suffit de lancer le serveur local, à l'aide de la commande suivante :
```		
python manage.py runserver
```
5. L'application est prête à être utilisée. Son fonctionnement correspond aux documents de conception fournis.
 
6. Dans la base de donnée communiquée, 4 comptes de démonstrations ont été créés avec quelques publications. Les noms d'utilisateurs sont les suivants :
```		
demoUser
```
```		
pierre_5
```
```		
françoise
```
```		
john1234
```
Le mot de passe est le même pour tous ces comptes :
```		
DummyUser2546
```
Pour avoir une bonne idée du fonctionnement de l'application, la connexion au compte demoUser est recommandée.
 
BONUS : Si vous souhaitez tester vous même la conformité à la PEP8, vous pouvez installer et exécuter flake8, à l'aide des commandes suivantes :
```		
pip install flake8
```
```		
flake8 --exclude=env --max-line-length=119 --format=html --htmldir=rapport
```
