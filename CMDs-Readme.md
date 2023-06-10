===================================================================================================
# CMDs | Quickstart
===================================================================================================
## Quick Python | Django Setup CMDs 
python -m venv venv <!-- or python -m venv env -->
venv\Scripts\activate.bat <!-- env\Scripts\activate.bat -->
venv\Scripts\deactivate <!-- To deactivate for Windows -->

sudo apt install python3-venv <!-- To install venv for Ubuntu -->
python3 -m venv venv <!-- To create for Ubuntu/Unix/MacOS    -->
source venv/bin/activate <!-- To activate venv for Ubuntu/Unix MacOS -->
deactivate <!-- To deactivate venv for Ubuntu/Unix MacOS -->

django-admin startproject core . <!-- To startproject -->
py manage.py startapp blogapi <!-- To startapp -->

py manage.py makemigrations <!-- To make migrations for db model(s) -->
py manage.py migrate <!-- To migrate db -->

py manage.py runserver <!-- To open at default port or: py manage.py runserver 8001 -->
py manage.py shell <!-- To run the shell -->
py manage.py createsuperuser <!-- To create super user -->

pip freeze > requirements.txt <!-- To freeze requirements.txt-->
pip install -r requirements.txt <!-- To install requirements.txt-->

pip install --upgrade pip
pip install django python-dotenv Pillow gunicorn
pip install djangorestframework django-cors-headers 
pip install psycopg2-binary mysqlclient djongo
<!-- For testing-->
pip install coverage
coverage run --omit='*/venv/*' manage.py test
coverage html

===================================================================================================
## React JS CMDs
===================================================================================================

npm install -g create-react-app <!-- To install reacjs globally -->
npm list react
<!-- npm update react react-dom -->
npx create-react-app frontend-react <!-- Create reacjs app -->
npx create-react-app . <!-- Create reacjs app at the cwd -->

npm install react-bootstrap
npm install bootstrap <!-- import 'bootstrap/dist/css/bootstrap.min.css'; -->
npm install @material-ui/core <!--  alternative to bootstrap -->

npm i react-router-dom@5.3.4
npm install redux react-redux

<!-- npm i --save react-redux@7.2.4 -->
npm install --save redux-devtools-extension
npm install @reduxjs/toolkit
npm install -g react-devtools
npm install react-phone-number-input <!-- phone number input form with country code -->

npm install axios react-router-dom@5.3.4 bootstrap redux react-redux react-bootstrap react-phone-number-input material-ui

===================================================================================================
# DevOps
===================================================================================================

## Docker && Docker Compose CMDs 
docker -v
docker version
docker ps -a
<!-- Build and run Docker Image: -->
docker pull <image-name>
docker images
docker rmi <image-name-or-id>
docker build -t <image-name-or-id> . <!-- To build image. Add `.` to build at cwd -->
docker run -p 8000:8000 <image-name-or-id> <!-- To run built image -->
<!-- Psshing Images to Docker Hub: -->
docker login
docker tag <image-name-or-id> <username>/<repository>:<tag>
docker push <username>/<repository>:<tag> 
docker tag djangoapi jondebosco/dockerized-djangoapi:v1.0
docker push jondebosco/dockerized-djangoapi:v1.0
<!-- Build and run Docker Image: -->
docker exec -it djangoapi_container /bin/bash
docker exec -it 8a2449609dee7b579 /bin/sh
docker exec -it 6343202eec sh
vi filename
i => insert mode
Esc => excape
:wq => save exit 
<!-- Docker Container CMD -->
docker start <contaner-name or id>
docker restart <contaner-name or id>
docker stop  <contaner-name or id>
docker kill <contaner-name or id>
docker logs <contaner-name or id>
docker inspect <contaner-name or id>
docker rename <contaner-name or id>
docker rm <contaner-name or id>
docker stats <contaner-name or id>
docker pause <contaner-name or id>
docker unpause <contaner-name or id>
docker inspect <contaner-name or id>
docker exec <contaner-name or id>
docker top <contaner-name or id>
<!-- Some Docker Compose CMDs -->
docker-compose run <image>
docker-compose run django-admin startproject core .
docker-compose build
docker-compose up
docker-compose up --build
docker-compose up -d
<!-- Some Docker Volume CMDs-->
docker volume ls
docker volume rm
---------------------------------------------------------------------------------------------------
## Docker Exec 'vi' CMDs:
1. i: Enter insert mode to start inserting text at the cursor position.
2. Esc: Exit insert mode and return to command mode.
3. :w: Save the changes made in the file.
4. :wq or :x: Save the changes and exit vi.
5. :q: Quit vi (exit) without saving changes.
6. :q!: Quit vi without saving changes, even if modifications were made.
7. yy or Y: Copy the current line (yank).
8. dd: Delete the current line.
9. p: Paste the copied or deleted content.
10. /search_text: Search for the specified text.
11. n: Find the next occurrence of the searched text.
12. N: Find the previous occurrence of the searched text.
13. u: Undo the last change.
14. Ctrl + r: Redo the last undone change.
15. :s/old/new: Substitute the first occurrence of "old" with "new" in the current line.
16. :s/old/new/g: Substitute all occurrences of "old" with "new" in the current line.
17. :%s/old/new/g: Substitute all occurrences of "old" with "new" in the entire file.
18. :set number: Display line numbers.
19. :set nonumber: Hide line numbers.
20. :help: Open the built-in help system.
21. gg: Go to the first line of the file.
22. G: Go to the last line of the file.
23. :n: Go to line number "n".
24. Ctrl + f: Scroll forward one page.
25. Ctrl + b: Scroll backward one page.
26. :e filename: Open another file for editing without leaving vi.
27. Ctrl + g: Display the current file name and position.
28. Ctrl + u: Scroll half-page up.
29. Ctrl + d: Scroll half-page down.
30. Ctrl + o: Jump to the previous location.

---------------------------------------------------------------------------------------------------
## Kubernetes CMDs:
<!-- Some verison check CMDs-->
kubectl version 
kubectl version --output=json
kubectl version --output=yaml
kubectl config get-contexts
<!-- Minikube Insallation CMDs-->
choco install kubernetes-cli
choco install minikube
minikube version
<!-- minikube start -->
minikube status
minikube dashboard
<!-- Debugging Minikube - Docker conflict-->
docker system prune
minikube delete
minikube start --driver=docker
minikube start --force --driver=docker
minikube dashboard --logtostderr --v=2
minikube dashboard --url
<!-- To restart the Docker service: -->
Press Win + R to open the Run dialog box.
Type services.msc
<!-- Here are some of the most commonly used Kubernetes commands: -->
1. kubectl create: Creates a resource from a file or stdin.
   Example: kubectl create -f deployment.yaml

2. kubectl apply: Creates or updates a resource from a file, directory, or stdin.
   Example: kubectl apply -f deployment.yaml

3. kubectl get: Retrieves information about resources.
   Example: kubectl get pods

4. kubectl describe: Displays detailed information about a resource.
   Example: kubectl describe pod my-pod

5. kubectl logs: Retrieves the logs of a container in a pod.
   Example: kubectl logs my-pod

6. kubectl exec: Executes a command in a container in a pod.
   Example: kubectl exec -it my-pod -- /bin/bash

7. kubectl delete: Deletes resources.
   Example: kubectl delete pod my-pod

8. kubectl scale: Changes the number of replicas of a deployment or replicaset.
   Example: kubectl scale deployment/my-deployment --replicas=3

9. kubectl rollout: Manages the rollout of changes to a deployment.
   Example: kubectl rollout status deployment/my-deployment

10. kubectl port-forward: Forwards one or more local ports to a pod.
    Example: kubectl port-forward pod/my-pod 8080:80

11. kubectl create secret: Creates a secret.
    Example: kubectl create secret generic my-secret --from-literal=KEY=VALUE

12. kubectl create configmap: Creates a config map.
    Example: kubectl create configmap my-config --from-file=app-config.yaml

13. kubectl apply -f: Applies a configuration file to create or update resources.
    Example: kubectl apply -f deployment.yaml

14. kubectl edit: Edits a resource in the default editor.
    Example: kubectl edit deployment/my-deployment

15. kubectl label: Adds or updates labels of a resource.
    Example: kubectl label pod/my-pod environment=production

---------------------------------------------------------------------------------------------------
## AWS CLI | ECR CMDs:
<!-- Pushing Docker Image from Docker Hub to AWS ECR -->
Create Groups | e.g. admin-group
Create Users  | e.g. admin
Create Roles  | e.g. admin-role
Create Policies | Add desired policy names/inline policies
<!-- Install awscli -->
pip install awscli
<!-- Aftter crating ecr repo click on `Push commands` for docker => ecr django-api -->
<!-- Create an IAM user and get ecr-djangoapi_credentials.csv -->
<!-- Some Major Policy Names an admin user -->
1. AmazonEC2FullAccess
2. AmazonS3FullAccess
3. AmazonRDSFullAccess
4. AdministratorAccess-AWSElasticBeanstalk
5. AmazonEC2ContainerRegistryFullAccess
<!-- Some Inline Policies -->
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "rds:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "elasticbeanstalk:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ecr:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ecs:*"
      ],
      "Resource": "*"
    }
  ]
}
<!-- Goto Security Credentials -->
<!-- Create access key -->
<!-- Then run: -->
aws configure
AWS Access Key ID [****************POHU]: AKIAVUDETP7MQFFEKFNU
AWS Secret Access Key [****************QbQT]: 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
Default region name [None]: region=us-east-1
Default output format [None]: output=json
<!-- Retrieve an authentication token and authenticate your Docker client to your registry.
Use the AWS CLI to login in the terminal: -->
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/h9x1m6c8
<!-- Note: If you receive an error using the AWS CLI, make sure that you have the latest version of the AWS CLI and Docker installed. -->
<!-- Pull the image to local env from hub? -->
docker pull jondebosco/django-api
<!-- Or build your the Docker image using the following command. For information on building a Docker file from scratch see the instructions here . You can skip this step if your image is already built: -->
docker build -t ecr-django-api .
<!-- After the build completes, tag your image so you can push the image to this repository: -->
docker tag ecr-django-api:latest public.ecr.aws/h9x1m6c8/ecr-django-api:latest
docker tag jondebosco/django-api:latest public.ecr.aws/h9x1m6c8/ecr-django-api:v1.0

docker tag djangoapi:latest public.ecr.aws/h9x1m6c8/ecr-djangoapi:latest
docker push public.ecr.aws/h9x1m6c8/ecr-djangoapi:latest
<!-- Run the following command to push this image to your newly created AWS repository: -->
docker push public.ecr.aws/h9x1m6c8/ecr-django-api:v1.0
---------------------------------------------------------------------------------------------------
## AWS ECR / ECS to Elastic Beanstalk | EC2 | S3
<!-- Create EB acc -->
create EC2 key-pair
PuTTY-User-Key-File-2: ssh-rsa
Encryption: none
Comment: admin-key-pair
Public-Lines: 6
AAAAB3NzaC1yc2EAAAADAQABAAABAQC5bJSEMsG2rmBCGlqf4qhjVZ7nr5BPAiLC
bTGNrTqHmgwHU/oY6thayvVaGq0WfMrDIYuqGhdcrGRX+WbqoJppYwNFoI5nD/VL
DzIzwMfm/KI74TL/T37OCAQoaolwwh+yeiTLD5Bjm4bw+bdHgo2fnu+6SpQS0J7T
JyqLNMt6vqdNz20IQOmNS+ur3ghc+j4Z1DW4zAvtDXvlZ/XdeAmtdulUGq20DbQv
lF9L/PATnYZIFOHdzzioJzcggGUQBaaZi8ZwLmT+wLAkjoLu4LEGlg1kxXtr1Ra1
ZvgYno/yGQW3784NNx5GOkbV94s9JblD3DZfagpblar68Q2co5hX
Private-Lines: 14
AAABACUr4TIHQtIubtmRku1OcNdJCMwFY/aSxQkY/sAaJAufFB479X0dRzYcTcc8
ZcqGRdeMWAVHqbtIS+1e8ATFIW9TDArfPuzmRBRB/ZxmXyytJJDAeoq4EwGWlc7M
XLUgFV6gIdQbUKTHPuv8A4PwZhfDsuczoC+NZumJhnvVn50BV+3apNsseR8VsB+K
e8vrvgHNHo91vjnZirRuWwrfqr4gYt1eRNAGIT/edT/tuCd13IvR4efXa9X7aC9H
9tcyRmd5qgoQCKXTZq9tcfD8sZQpGK5t5TUaI+kEUPnxUwua9yYoLBBNud+0qZFY
UZdrR0P5UaDXgvImswXDX6q2skEAAACBAOUcSHkUW9bCibXCYvV1qECqPmSPXzBI
L8EBQSsPr/ePulvcEoYw+NDcA1IQxzf4/C6WijrNiNGvePf9cMUmb8D8fpY5sUcP
twcqMgos4Jcb7H3uiuQbB66j9FqOtpU2rdu+b74axsfPOt0oAEItHjzfEvT1zlx1
mDq9n2ObL6+HAAAAgQDPL7ksMPmu6wy9Cgxyw6HDzokRBhyVgRho0aidVvv8zZcf
B7IQZYX08PnSnIpSy6zCyrVevSnDz9CdoMdA1vmDrzXsIs6XXrBANT5mAR70huI1
LOnPueF08epze+jlPbK9JVsTGCqxeRd41s9IcbZfw781cgDuDRWxx5SCpLHksQAA
AIBTWCLV/+rC5PaNb3Ck4wQwTT3WGxze1htiXNw6H07LcaBkWL3lGLvWVf9bI5AX
14NWqmtUzdug+nFgX8F5pEKApiuZE9GHZbPVhjXc7oe8icm6DWEXqBl03w91k80g
rgD4wWM6Y75qPpyMtMe178T/GA5oud+J2X+hX7muvU1f7g==
Private-MAC: 37b5e0e4886ce86b514453fa49889401d1b92c2e

---------------------------------------------------------------------------------------------------
## Nano CMDs 
1. Ctrl + G: Display the help menu with a list of available commands.
2. Ctrl + O: Save the current file (write Out).
3. Ctrl + X: Exit Nano. If changes were made, it prompts to save the file first.
4. Ctrl + K: Cut the current line and store it in the cut buffer.
5. Ctrl + U: Paste the contents of the cut buffer.
6. Ctrl + W: Search for a string within the file.
7. Ctrl + \: Search and replace a string within the file.
8. Ctrl + C: Show the current cursor position (Help menu).
9. Ctrl + _ (underscore): Go to a specific line number.
10. Ctrl + R: Insert the contents of another file at the cursor position.
11. Ctrl + J: Justify the current paragraph.
12. Ctrl + A: Move the cursor to the beginning of the current line.
13. Ctrl + E: Move the cursor to the end of the current line.
14. Ctrl + Y: Scroll up one page.
15. Ctrl + V: Scroll down one page.
16. Ctrl + P: Move the cursor to the previous line.
17. Ctrl + N: Move the cursor to the next line.
18. Ctrl + F: Move the cursor one character forward.
19. Ctrl + B: Move the cursor one character backward.
20. Alt + \ (backslash): Go to the first line of the file.
21. Alt + /: Go to the last line of the file.
22. Alt + . (period): Toggle between inserting the current date and time.
23. Alt + U: Undo the last action.
24. Alt + E: Redo the last undone action.
25. Alt + A: Mark text for block manipulation.
26. Alt + 6: Copy the marked text to the cut buffer.
27. Alt + W: Toggle automatic line wrapping.
28. Alt + M: Toggle mouse support (if enabled in the terminal).
29. Alt + H: Show/hide line numbers.
30. Alt + Space: Set/unset the mark.
===================================================================================================
Databases
===================================================================================================
## postgres CMDs
<!-- CONNECTIONS -->
psql -h localhost -p 5432 -U jb -d gpt  <!-- -- To connect in cmd: -->
psql -U jb -d tiktok
\c gpt <!-- -- To connect to a diff db: -->

<!-- DATABASE OPERATIONS-->
CREATE DATABASE [db_name]; <!-- -- To create db: -->
DROP DATABASE [db_name]; <!-- -- To drop db: -->

<!-- TABLES OPERATIONS -->
\l <!-- -- To view db: -->
\d <!-- -- To view list of tables and sequence: -->
\dt <!-- -- To view tables: -->
\dt+ <!-- -- To view table plus extra info: -->
\dc [db_name] <!-- -- To list specific table: -->

<!-- -- TO CREATE TABLE-->
CREATE TABLE users (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(50),
    Age INTEGER,
    Email VARCHAR(255)
);

or 

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  age INTEGER CHECK (age > 0)
);

<!-- -- TO INSERT INTO TABLE-->
<!-- --single -->
INSERT INTO users (username, age, email, password)
VALUES ('Jon', 34, 'jon@example.com','jon12345');
<!-- --multiple -->
INSERT INTO persons (username, password, age, email)
VALUES ('Jay B', 35, 'jay.smith@example.com'),
       ('Jane Doe', 25, 'jane.doe@example.com'),
       ('Bob Johnson', 42, 'bob.johnson@example.com');

<!-- TO ALTER TABLE -->
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(255)
);

<!-- SELECT -->
<!-- -- To select from table: -->
SELECT * FROM teachers;

ALTER TABLE employees 
    ALTER COLUMN first_name SET DATA TYPE TEXT,
    ALTER COLUMN email SET DATA TYPE VARCHAR(255),
    ALTER COLUMN first_name SET NOT NULL,
    ALTER COLUMN email SET NOT NULL,
    ADD CONSTRAINT unique_email UNIQUE (email),
    ALTER COLUMN password SET NOT NULL;

<!-- TO ALTER TABLE -->
UPDATE users
SET first_name = 'Joy', last_name = 'Mary'
WHERE id = 15;
<!-- --To update a multiple tables: -->
UPDATE users
SET
  name = CASE
           WHEN id = 8 THEN 'Jane Doe'
           WHEN id = 9 THEN 'Bob Johnson'
         END,
  age = CASE
          WHEN id = 8 THEN 25
          WHEN id = 9 THEN 30
        END,
  email = CASE
            WHEN id = 8 THEN 'jane@example.com'
            WHEN id = 9 THEN 'bob@example.com'
          END,
  password = CASE
               WHEN id = 8 THEN 'jane12345'
               WHEN id = 9 THEN 'bob12345'
             END
WHERE id IN (8, 9);

<!-- DELETE -->
<!-- --To delete a single row: -->
DELETE FROM users WHERE id = 10;
DELETE FROM users WHERE email = 'jay@example.com';
<!-- --To delete a multiple row: -->
DELETE FROM users WHERE id BETWEEN 17 AND 18;
<!-- --To delete a diff num of row: -->
DELETE FROM users WHERE id IN (2, 5, 9);
<!-- --To delete a last row: -->
DELETE FROM tablename
WHERE primary_key = (SELECT max(primary_key) FROM tablename);
<!-- --To delete all -->
DELETE FROM users;
<!-- --To drop all -->
DROP TABLE users;
<!-- -- View the last inserted row b4 delete-->
SELECT * FROM users ORDER BY id DESC LIMIT 1;
<!-- -- Delete the last inserted row -->
DELETE FROM users WHERE id = (SELECT id FROM users ORDER BY id DESC LIMIT 1) RETURNING *;


<!-- BACKUP -->
--psql -h localhost -p 5432 -U analysis -d postgres
pg_dump -U username -h hostname databasename > backup.sql
pg_dump -U jb -h localhost gpt > backup_users.sql
<!-- To restore: -->
pg_restore --dbname=mydatabase mydb.backup
pg_restore jb=gpt mydb.backup
---------------------------------------------------------------------------------------------------
## mysql CMDs
<!-- CONNECTION -->
mysql -u username -p <!-- -- To run mysql in cmd -->
<!-- DATABASE -->
CREATE DATABASE dbname; <!-- -- To create db -->
SHOW DATABASES; <!-- -- To view db -->
SELECT database(); <!-- -- To view db in use -->
USE dbname; <!-- -- To use db -->

<!-- TABLE -->
<!-- -- To create table -->
CREATE TABLE 
<!-- -- To view table -->
SHOW TABLES;

SELECT * FROM table_name;

<!-- USER -->
SELECT USER(); <!-- -- To view current user -->
SELECT User, Host FROM mysql.user; <!-- -- To view all users -->
<!-- TO BACKUP -->
mysqldump -u jb -p tiktok > tiktok_backup.sql
<!-- TO TRUNCATE | DROP  -->
TRUNCATE TABLE table_name; <!-- -- Empty the tables: Use the TRUNCATE TABLE SQL command to delete -- all the data from the tables in the database. -->
DROP DATABASE tiktok; <!-- -- Drop the database: Finally, use the DROP DATABASE SQL command to delete the entire database. -->
---------------------------------------------------------------------------------------------------
## mongo CMDs
<!-- REMOTE CONNECTION -->
<!-- -- Start the Mongo Shell -->
mongosh "YOUR_CONNECTION_STRING" --username YOUR_USER_NAME
mongosh "mongodb+srv://cluster0.p70vwar.mongodb.net/JonDeBosco" --apiVersion 1 --username JonDeBosco
<!-- -- Check monosh Version -->
mongosh --version

<!-- LOCALHOST CONNECTION -->
mongosh <!-- mongodb://localhost:27017 -->

<!-- DATABASE OPERATIONS -->
db <!-- -- To show Current Database -->
show dbs <!-- -- To show All Databases -->
use dbname <!-- -- To Create Or Switch Database -->
<!-- -- To rename a db -->
<!-- -- // create a new database with the desired name -->
use new_db
<!-- -- // copy the contents of the old database to the new one -->
db.copyDatabase('old_db', 'new_db')
<!-- -- // drop the old database -->
use old_db
db.dropDatabase() <!-- -- Drop Database -->

<!-- COLLECTIONS -->
show collections
db.createCollection('posts') <!-- -- Create Collection -->
db.collection.renameCollection( newName, { dropTarget: <boolean> } ) <!-- -- To Rename a collection -->
<!-- -- To delete collection -->
db.posts.drop()
<!-- -- Insert Document -->
db.posts.insertOne({
  title: 'Post 1',
  body: 'Body of post.',
  category: 'News',
  likes: 1,
  tags: ['news', 'events'],
  date: Date()
})
<!-- -- Insert Multiple Documents -->
db.posts.insertMany([
  {
    title: 'Post 2',
    body: 'Body of post.',
    category: 'Event',
    likes: 2,
    tags: ['news', 'events'],
    date: Date()
  },
  {
    title: 'Post 3',
    body: 'Body of post.',
    category: 'Tech',
    likes: 3,
    tags: ['news', 'events'],
    date: Date()
  }
])
<!-- -- Find All Documents -->
db.posts.find()
<!-- -- Find Documents with Query -->
db.posts.find({ category: 'News' })

<!-- USERS -->
show users <!-- -- To view users -->
<!-- CREATING USERS -->
db.createUser({
  user: "your_username",
  pwd: "your_password",
  roles: [{ role: "readWrite", db: "your_database_name" }]
})
<!-- -- Creating superuser: -->
use admin
db.createUser({
  user: "your_superuser_username",
  pwd: "your_superuser_password",
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "root", db: "admin" }
  ]
})

db.createUser({
  user: "jb",
  pwd: "boz1234567",
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "root", db: "admin" }
  ]
})
<!-- -- Switching users: -->
db.auth('myuser', 'mypassword')

<!-- -- To show the current user -->
 db.getUsers()

--  To update users
db.updateUser(
   "myuser",
   {
     roles: [ { role: "readWrite", db: "mydatabase" } ]
   }
)

db.updateUser(
  "superuser", {
    roles: [{
      role: "userAdminAnyDatabase", db: "admin"}, {
      role: "dbOwner", db: "mydatabase"}]
    }
)

db.updateUser(
  "jb", {
    roles: [
      {role: "userAdminAnyDatabase", db: "admin"}, 
      {role: "dbOwner", db: "tiktok"}]
    }
)
===================================================================================================
## GIT & GITHUB
===================================================================================================
<!-- ### Create local repo and commit -->
git status
git init 
git init -b main
git add . <!--to add all files or `git add CMDs-Readme.md` -->
git commit -m "First commit"
<!-- git commit -m "updated Readme.md"
git commit -m "added  requirements.txt" -->

<!-- Create Remote Repo -->
<!-- ### Push to remote repo -->
git remote add <remote-url>
git branch -M -main
git push -u origin main

<!-- ### Update to remote repo -->
git remote -v
git push origin main

<!-- ### To reinitialize -->
ls -a
rm -rf .git

<!-- ### Git Branching and Checkout -->
git branch <!--To see local -->
git branch -r <!--To see remote... git checkout <remote-branch-name> -->
git branch -a <!--To see both -->

===================================================================================================
## Others
===================================================================================================
<!-- ## Some Useful CMDs -->
rm -rf <target-name> <!--To remove a dir  -->
mv <old-name> <new-name> <!--To rename a dir -->
===================================================================================================
<!-- ### Creating venv using built-in python -m venv: -->

##### For Windows 
<!--To create venv -->
python -m venv venv  <!-- or python -m venv env -->
<!--To activate venv for cmd -->
venv\Scripts\activate.bat
<!-- env\Scripts\activate.bat -->
<!-- venv\Scripts\Activate.ps1 (for powershell) -->
<!--To set powershell as default, run: "Set-ExecutionPolicy RemoteSigned" -->
venv\Scripts\deactivate <!-- To deactivate for Windows -->
<!-- env\Scripts\deactivate -->
##### For Ubuntu/Unix MacOS
<!-- , Install the python3-venv package if it is not installed -->
sudo apt install python3-venv <!-- (Ubuntu) -->
<!-- Create a virtual environment using the python3 -m venv command: -->
python3 -m venv venv <!-- For Ubuntu/Unix   -->
<!-- Activate the virtual environment using the source command: -->
source venv/bin/activate
##### Alternatively, create venv using third-party "virtualenvwrapper":
pip install virtualenvwrapper
mkvirtualenv venv <!--To create the virtualenv -->
workon venv <!--To activate venv -->
<!-- To deactivate -->
deactivate <!-- To deactivate for Ubuntu/Unix MacOS -->

---------------------------------------------------------------------------------------------------

#### To view the installed moudules in the venv
pip show django <!--for cmd -->
pip freeze

#### Install django
pip install django

#### Creating projct
django-admin startproject api .

<!-- cd tiktok if thus added a dot after "django-admin startproject tiktok ." -->
#### Creating app(s)
py manage.py startapp drf_react_jwt
<!-- py manage.py startapp profiles -->
<!-- py manage.py startapp products -->
<!-- py manage.py startapp app -->

#### Installing djangorestframework
pip install djangorestframework

#### Open the settings.py file and add to the INSTALLED_APPS section:
INSTALLED_APPS = [    
...    
'rest_framework',    
'post',
]

#### Makiing makemigrations
py manage.py makemigrations
<!-- 
py manage.py makemigrations visualization
py manage.py makemigrations products
py manage.py makemigrations blog
 -->
py manage.py migrate
<!-- To rollback migrations:
py manage.py showmigrations email_otp
py manage.py migrate email_otp 0001

py manage.py migrate blog
 -->

<!-- Error: unpon running -> py manage.py makemigrations
It is impossible to add a non-nullable field 'user' to smsotp without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.      
Select an option: -->

#### Running server
<!-- To open at default port: 8000 -->
py manage.py runserver
<!-- To open at a custom port: py manage.py runserver 8001 -->

<!-- To run the shell -->
py manage.py shell

<!-- py manage.py reset_db -->


#### Creating superuser
py manage.py createsuperuser

#### Freezing and Installing requirements
<!-- To freeze -->
pip freeze > requirements.txt
<!-- To install -->
pip install -r requirements.txt

<!-- pip install wheel
pip install tzdata
pip install --upgrade pip

pip install backports.zoneinfo
git clone https://github.com/pganssle/zoneinfo.git
cd zoneinfo
pip install .

pip install backports.zoneinfo;python_version<"3.9" -->

<!-- AUth css -->
pip install django-crispy-forms

#### Installing cors
pip install django-cors-headers

#### Connecting to db (psql)
pip install psycopg2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tiktok',
        'USER': 'jb',
        'PASSWORD': 'boz1234567',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#### Connecting to db (mysql)
pip install mysqlclient

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tiktok',
        'USER': 'jb',
        'PASSWORD': 'boz1234567',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#### Connecting to db (mongodb)

pip install pymongo djongo dnspython

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mydatabase',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'localhost',
            'username': 'myuser',
            'password': 'mypassword',
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1',
        },
    },
}

Localhost conn:

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mydatabase',
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
        },
    }
}

Add djongo to your project's INSTALLED_APPS setting in settings.py:

INSTALLED_APPS = [
    # ...
    'djongo',
    # ...
]

#### .env and .gitignore files handling
<!-- Step 1: Install python-dotenv -->
pip install python-dotenv
<!-- Step 2: Create a .env file in the root directory of your Django project.-->
mkdir .env
<!-- Step 3: Add sensitive information to .env file -->
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port

or

MONGODB_NAME=your_mongodb_database_name
MONGODB_USER=your_mongodb_username
MONGODB_PASS=your_mongodb_password
MONGODB_HOST=your_mongodb_host
MONGODB_PORT=your_mongodb_port
<!-- Replace "your_secret_key", "your_db_name", "your_db_user", "your_db_password", "your_db_host", and "your_db_port" with your actual secret key and database details. -->
<!-- Step 4: Load .env file in Django settings.py -->
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

DATABASES = {
     'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
     }
}

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv('MONGODB_NAME'),
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': os.getenv('MONGODB_HOST'),
            'port': int(os.getenv('MONGODB_PORT')),
            'username': os.getenv('MONGODB_USER'),
            'password': os.getenv('MONGODB_PASS'),
            'authSource': 'admin',
            # 'authMechanism': 'SCRAM-SHA-1',
        },
    },
}

<!-- import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('MONGODB_NAME'),
        'USER': os.getenv('MONGODB_USER'),
        'PASSWORD': os.getenv('MONGODB_PASS'),
        'HOST': os.getenv('MONGODB_HOST'),
        'PORT': os.getenv('MONGODB_PORT'),
    }
} -->

<!-- Step 5: Add .env file to .gitignore -->
mkdir .gitignore
<!-- Open the .gitignore file and add the following line to it: -->
.env


py manage.py shell


CLI Error:
You must either define the environment 
variable DJANGO_SETTINGS_MODULE or call 
settings.configure() before accessing settings.

Fix:
export DJANGO_SETTINGS_MODULE=mysite.settings
export DJANGO_SETTINGS_MODULE=tiktok.settings
python manage.py runserver

or

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiktok.settings')
django.setup()

# Now you can import your models, serializers, views, etc.
from rest_framework import serializers
from post.models import Post
from myapp.serializers import BookSerializer
# ...

<!-- Ex1: -->
>>> import os
>>> import django
>>> os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
>>> django.setup()
>>> from rest_framework import serializers
>>> from bookapp.models import Book

<!-- Ex2: -->
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiktok.settings')
django.setup()

from sms_otp.models import SmsOtp
from sms_otp import views

from email_otp.models import EmailOTP
from email_otp import views

from email_link_auth.models import EmailVerification
from email_link_auth import views

from visualization.models import Sales
from visualization import views

from drf.models import Book
from drf import views

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
import random
import uuid

from customers.models import Customer
Customer.objects.all()


smsotp = SmsOtp.objects.all()
print(smsotp)

for obj in SmsOtp.objects.iterator():
    print(obj)

smsotp = SmsOtp.objects.all()[:5]
print(smsotp)

##### Fetching ids/values
smsotp = SmsOtp.objects.all()
id_list = smsotp.values_list('id', 'code', flat=True)
print(id_list)

SmsOtp.objects.all().values_list('id', 'code')

# Fetching the first item
smsotp = SmsOtp.objects.filter().first()
print(smsotp)

smsotp = SmsOtp.objects.filter().last()
print(smsotp)

smsotp = SmsOtp.objects.filter(id=4).exists()
print(smsotp)


##### Fetching all var names
var_names = [field.name for field in SmsOtp._meta.get_fields()]
print(var_names)

# Deleting itmens
smsotp = SmsOtp.objects.filter().first()
print(smsotp)
smsotp.delete()
print(smsotp)

smsotp = SmsOtp.objects.filter(id=33).first()
print(smsotp)

smsotp.delete()
print(smsotp)

# More fetching queries
smsotp = SmsOtp.objects.filter(created_at__gte='2023-03-27')
print(smsotp)

smsotp = SmsOtp.objects.filter(created_at__lt='2023-03-27')
print(smsotp)

smsotp = SmsOtp.objects.filter(code=780145)
print(smsotp)


# More drills...

smsotp = SmsOtp.objects.filter(id=1).first()
print(smsotp)

smsotp = SmsOtp.objects.filter().exists()
print(smsotp)

smsotp = SmsOtp.objects.filter(code=695042).first()
print(smsotp)

smsotp = SmsOtp.objects.filter(code=otp, phone=phone).exists()
print(smsotp)

SmsOtp.objects.values('phone')

##### Editing & Saving
smsotp = SmsOtp.objects.filter().first()
print(smsotp)
smsotp.code = 123456
smsotp.save()
print(smsotp)

#### Getting and checking 
smsotp = SmsOtp.objects.get(id=48)
print(smsotp)

# Worked!

otp = 589797
smsotp = SmsOtp.objects.filter(code=otp).first()
if smsotp:
    smsotp.is_verified = True
    smsotp.save()
    print("Phone number verification is succussful!")
else:
    print("OTP is wrong or expired!")

#### Deleting OTP afterwards

otp = 589797
smsotp = SmsOtp.objects.filter(code=otp).first()
if smsotp:
    smsotp.is_verified = True
    smsotp.delete()
    print("Phone number verification is succussful!")
else:
    print("OTP is wrong or expired!")
###### AttributeError: 'str' object has no attribute 'delete'

#### Stting OTP None afterwards
otp = 589797
smsotp = SmsOtp.objects.filter(code=otp).first()
if smsotp:
    smsotp.is_verified = True
    smsotp.code = None
    smsotp.save()
    print("Phone number verification is succussful!")
else:
    print("OTP is wrong or expired!")

smsotp = SmsOtp.objects.filter(code=695042).exists()
print(smsotp)


<!-- books = Book.objects.filter(published_date__lte='2010-01-01')

books = Book.objects.filter(Q(author='John Doe') | Q(author='Jane Doe'))

# Get the first 5 books in alphabetical order
books = Book.objects.order_by('title')[:5] -->


# Using get_object_or_404 methed
smsotp = get_object_or_404(SmsOtp, id=4)
print(smsotp)

EmailOTP.objects.all().delete()
EmailOTP.objects.filter().first().delete()

emailotp = EmailOTP.objects.filter(code=otp).first()
emailotp = EmailOTP.objects.filter().first()
emailotp = EmailOTP.objects.get(id=1).exists()
print(emailotp)


EmailOTP.objects.filter().first()

email_otp.created_at


otp = 932220

email_otp = EmailOTP.objects.filter(
    code=otp, 
    email=email, 
    is_verified=False, 
    created_at__gte=timezone.now() - timezone.timedelta(minutes=15)
).first()

if email_otp:
    email_otp.is_verified = True
    #emailotp.code = None
    email_otp.save()
    print("Email verification is succussful!")
else:
    print("OTP is wrong or expired!")


#### User model 

User.objects.all()
User.objects.filter(is_superuser=False).delete()
<!-- User.objects.all().delete() -->
User.objects.filter().last()
User.objects.filter().first()

user_id=37
User.objects.get(id=user_id)
user.id

user = User.objects.create(username='jay bul')
email = 'chibuzo.okenwa@gmail1.com'
code = str(random.randint(100000, 999999))
email_otp = EmailOTP.objects.create(user=user, email=email, code=code)
print(email_otp)


User.objects.filter().last()

CustomUser.objects.filter().last()


users_values = CustomUser.objects.all().values('first_name', 'email', 'phone')
for user in users_values:
    print(user['first_name'], user['email'], user['phone'])


users_values_list = CustomUser.objects.all().values_list('first_name', 'email', 'phone')
for user in users_values_list:
    print(user[0], user[1], user[2])

print('\nFirst Name:', user[0], '\nEmail:', user[1], '\nPhone:', user[2])

### DELETING ACCOUNT 2

<!-- from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from myapp.models import Profile -->

<!-- from django.contrib.auth.models import User
from django.http import HttpRequest
from myapp.views import delete_user_view -->

# Create a test user
user = User.objects.create_user('testuser', password='testpassword')

# Create a mock request object
request = HttpRequest()

# Call the view function with the user's ID
response = delete_user_view(request, user.id)

def delete_user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    # Delete all profiles associated with the user
    Profile.objects.filter(user=user).delete()
    # Delete the user
    user.delete()
    return redirect('home')  # or any other desired URL

<!-- from django.urls import path
from myapp.views import delete_user_view -->

urlpatterns = [
    path('delete-user/<int:user_id>/', delete_user_view, name='delete_user'),
]

from email_otp import views

request = HttpRequest()
response = delete_user_view(request, user.id)


user.username
#user.request
#request.user

emailotp.user
emailotp.created_at
emailotp.code
emailotp.email
emailotp.is_verified





User.objects.filter(is_superuser=False).delete()
EmailVerification.objects.filter()

user = User.objects.create(username='ken')
email = 'chibuzo.okenwa@gmail.com'
token = uuid.uuid4()
email_otp = EmailVerification.objects.create(user=user, email=email, token=token)



EmailVerification.objects.filter()
User.objects.filter(is_superuser=False).delete()

Sales.objects.all()



User.objects.filter()

Book.objects.all()




#### Search

query = 'Ryonda'
Book.objects.filter(title__icontains=query)


query = 'Ken'

res_title = Book.objects.filter(title__icontains=query)
res_author = Book.objects.filter(author__icontains=query)

if res_title:
    print(res_title)
elif res_author:
    print(res_author)
else:
    print("Not found!")









##### Here are some other commonly used QuerySets for the User model in Django:
Get a single user by username:
user = User.objects.get(username='some_username')

Get all users:
users = User.objects.all()

for obj in User.objects.iterator():
    print(obj)

Get a count of all users:
user_count = User.objects.count()

Get all superusers:
superusers = User.objects.filter(is_superuser=True)

Get all active users:
active_users = User.objects.filter(is_active=True)

Get all users ordered by their join date:
users_ordered_by_join_date = User.objects.order_by('date_joined')

Get all users whose first name is "John":
johns = User.objects.filter(first_name='John')

Get all users who have not verified their email:
unverified_users = User.objects.filter(emailverified=False)

Get all users whose last login time was more than a week ago:
inactive_users = User.objects.filter(last_login__lte=timezone.now() - timezone.timedelta(minutes=1))



Send a message...
<!-- Verify your email address
Hi Chibuzo,
Please confirm that you want to use this email address with your Vonage APIs account. If you did not request this change, then feel free to ignore this email.

Verify new email address

Regards,
The Vonage API Team 

OR

Subject: Verify your email address

Dear [USER],

Thank you for signing up with our service. To complete your registration, please click on the link below to verify your email address:

[VERIFICATION LINK]

Please note that this link is valid for 24 hours. If you did not request this verification, please disregard this email.

Best regards,
[COMPANY NAME]


Subject: OTP Email Verification

Dear [USER],

Thank you for signing up with our service. To complete your registration, please use the OTP code provided below:

OTP: [CODE]

This code is valid for 10 minutes. If you did not request this code, please disregard this email.

Best regards,
[COMPANY NAME]
-->




### Give steps to build Django REST Framework and connect to MySQL database and perform CRUD operations. Detailed clear code example 

Sure, here are the steps to build a Django REST Framework (DRF) project and connect to a MySQL database to perform CRUD operations:

#### Create a new Django project by running the following command in your terminal:
django-admin startproject myproject

#### Create a new Django app by running the following command in your terminal:
python manage.py startapp myapp

##### Install the necessary packages by running the following command in your terminal:
pip install django djangorestframework mysqlclient

#### Open the settings.py file in your project directory and add the following code to the INSTALLED_APPS section:

INSTALLED_APPS = [    ...    'rest_framework',    'myapp',]

#### In the settings.py file, configure the database connection to MySQL by adding the following code to the DATABASES section:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#### Replace mydatabase, myuser, mypassword, localhost, and 3306 with your own MySQL database details.

#### Create a new model in your app's models.py file. Here's an example:
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def str(self):
        return self.name

#### Create a new serializer in your app's serializers.py file. Here's an example:
from rest_framework import serializers
from .models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = 'all'

#### Create a new viewset in your app's views.py file. Here's an example:
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

#### In your app's urls.py file, add the following code to set up the URLs for your views:
from django.urls import path, include
from rest_framework import routers
from .views import MyModelViewSet

router = routers.DefaultRouter()
router.register(r'mymodels', MyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#### Run the migrations to create the table in your MySQL database by running the following command in your terminal:
python manage.py makemigrations
python manage.py migrate

#### Start the Django development server by running the following command in your terminal:
python manage.py runserver

#### You can now perform CRUD operations on your MyModel objects by making requests to the following URLs:

GET /mymodels/: Retrieve a list of all MyModel objects
POST /mymodels/: Create a new MyModel object
GET /mymodels/{id}/: Retrieve a specific MyModel object by ID
PUT /mymodels/{id}/: Update a specific MyModel object by ID
PATCH /mymodels/{id}/: Partially update a specific MyModel object by ID
DELETE /mymodels/{id}/: Delete a specific MyModel object by ID

#### Here's an example of how to use these URLs to perform CRUD operations using cURL:

#### Retrieve all MyModel objects:
curl http://localhost:8000/mymodels/

#### Create a new MyModel object:
curl -X POST -H 'Content-Type: application/json' -d '{"name": "My Object", "description": "This is my object."}' http://localhost:8000/mymodels/

Retrieve a specific MyModel object by ID:
curl http://localhost:8000/mymodels/1/

#### Update a specific MyModel object by ID:
curl -X PUT -H 'Content-Type: application/json' -d '{"name": "My Updated Object", "description": "This is my updated object."}' http://localhost:8000/mymodels/1/

#### Partially update a specific MyModel object by ID:
curl -X PATCH -H 'Content-Type: application/json' -d '{"name": "My Partially Updated Object"}' http://localhost:8000/mymodels/1/

#### Delete a specific MyModel object by ID:
curl -X DELETE http://localhost:8000/mymodels/1/
I hope this example helps you get started with building a DRF project and connecting to a MySQL database to perform CRUD operations. Let me know if you have any further questions or concerns!

ChatGPT Feb 13 Version.







#### DRF & MongoDB CRUD Operations.

Show fully step by step how to connect DRF to MongoDB database and perform CRUD operations with detailed code examples and outputs

Sure! Here's a step-by-step guide on how to connect Django REST framework (DRF) to MongoDB database and perform CRUD operations with detailed code examples and outputs.

#### Step 1: Install Required Packages
The first step is to install the necessary packages for working with MongoDB and Django REST framework. Here are the packages you need to install:

pymongo: Python driver for MongoDB.
djongo: Django connector for MongoDB.
djangorestframework: Django package for building RESTful APIs.

##### You can install these packages using pip. Run the following command in your terminal:
pip install pymongo djongo djangorestframework

#### Step 2: Configure Django Project
#### The next step is to configure your Django project to work with MongoDB. Here's what you need to do:

Add djongo to your project's INSTALLED_APPS setting in settings.py:

INSTALLED_APPS = [
    # ...
    'djongo',
    # ...
]

#### Configure the database settings in settings.py. Here's an example configuration for a MongoDB database named mydatabase:

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mydatabase',
        'ENFORCE_SCHEMA': False,
    }
}

Note that the ENFORCE_SCHEMA setting is set to False here to allow for flexibility in the schema.

#### Step 3: Create a Model
The next step is to create a model for the data you want to store in MongoDB. Here's an example model for a Person:

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

#### Step 4: Create a Serializer
Next, create a serializer to convert between Python objects and JSON data. Here's an example serializer for the Person model:

from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

#### Step 5: Create Views for CRUD Operations
Now, create views to handle CRUD (Create, Read, Update, Delete) operations for the Person model. Here are the views you need:

#### Create a view to list all Person objects:

from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

#### Create a view to retrieve a single Person object:
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

#### Step 6: Register URLs
Finally, register the URLs for the views in urls.py. Here's an example urls.py file:

from django.urls import path
from .views import PersonList, PersonDetail

urlpatterns = [
    path('persons/', PersonList.as_view(), name='person-list'),
    path('persons/<int:pk>/', PersonDetail.as_view(), name='person-detail'),
]

#### Step 7: Start MongoDB and Run Django Server
Start MongoDB by running the following command in your terminal:

mongod

Then, start the Django server by running the following command:

python manage.py runserver

#### Step 8: Test CRUD Operations
Now that everything is set up, you can test the CRUD operations on the Person model. Here are some examples using curl to send HTTP requests:

Create a new person:
curl -H "Content-Type: application/json" -X POST -d '{"name": "Alice", "age": 25, "email": "alice@example.com"}' http://localhost:8000/persons/

Output:
{"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"}

Retrieve a person by ID:
curl http://localhost:8000/persons/1/

Output:
{"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"}

Update a person:
curl -H "Content-Type: application/json" -X PUT -d '{"name": "Alice Smith", "age": 26, "email": "alice.smith@example.com"}' http://localhost:8000/persons/1/

Output:
{"id": 1, "name": "Alice Smith", "age": 26, "email": "alice.smith@example.com"}

Delete a person:
curl -X DELETE http://localhost:8000/persons/1/

Output:
{}

Conclusion
In this guide, you learned how to connect Django REST framework (DRF) to MongoDB database and perform CRUD operations. You installed the required packages, configured your Django project, created a model and serializer, and implemented views for the CRUD operations. Finally, you tested the API using curl.






ChatGPT Feb 13 Version. Free Research Preview. Our goal is to make AI systems more natural and safe to interact with. Your feedback will help us improve.
New chat



<!-- Adding Images and Videos -->
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)













### Implementing Google login authentication in Django involves several steps. 
Here is a step-by-step guide:

<!-- https://django-allauth.readthedocs.io/en/latest/installation.html
Python package: -->
pip install django-allauth

settings.py (Important - Please note ‘django.contrib.sites’ is required as INSTALLED_APPS):

# Specify the context processors as follows:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Already defined Django-related contexts here

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
]

INSTALLED_APPS = [
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.agave',
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.amazon_cognito',
    'allauth.socialaccount.providers.angellist',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.asana',
    'allauth.socialaccount.providers.auth0',
    'allauth.socialaccount.providers.authentiq',
    'allauth.socialaccount.providers.azure',
    'allauth.socialaccount.providers.baidu',
    'allauth.socialaccount.providers.basecamp',
    'allauth.socialaccount.providers.battlenet',
    'allauth.socialaccount.providers.bitbucket',
    'allauth.socialaccount.providers.bitbucket_oauth2',
    'allauth.socialaccount.providers.bitly',
    'allauth.socialaccount.providers.box',
    'allauth.socialaccount.providers.cern',
    'allauth.socialaccount.providers.cilogon',
    'allauth.socialaccount.providers.clever',
    'allauth.socialaccount.providers.coinbase',
    'allauth.socialaccount.providers.dataporten',
    'allauth.socialaccount.providers.daum',
    'allauth.socialaccount.providers.digitalocean',
    'allauth.socialaccount.providers.dingtalk',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.disqus',
    'allauth.socialaccount.providers.douban',
    'allauth.socialaccount.providers.doximity',
    'allauth.socialaccount.providers.draugiem',
    'allauth.socialaccount.providers.drip',
    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.dwolla',
    'allauth.socialaccount.providers.edmodo',
    'allauth.socialaccount.providers.edx',
    'allauth.socialaccount.providers.eventbrite',
    'allauth.socialaccount.providers.eveonline',
    'allauth.socialaccount.providers.evernote',
    'allauth.socialaccount.providers.exist',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.feedly',
    'allauth.socialaccount.providers.figma',
    'allauth.socialaccount.providers.fivehundredpx',
    'allauth.socialaccount.providers.flickr',
    'allauth.socialaccount.providers.foursquare',
    'allauth.socialaccount.providers.frontier',
    'allauth.socialaccount.providers.fxa',
    'allauth.socialaccount.providers.gitea',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.globus',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.gumroad',
    'allauth.socialaccount.providers.hubic',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.jupyterhub',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.keycloak',
    'allauth.socialaccount.providers.lemonldap',
    'allauth.socialaccount.providers.line',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.mailchimp',
    'allauth.socialaccount.providers.mailru',
    'allauth.socialaccount.providers.mediawiki',
    'allauth.socialaccount.providers.meetup',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.nextcloud',
    'allauth.socialaccount.providers.odnoklassniki',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.openid_connect',
    'allauth.socialaccount.providers.openstreetmap',
    'allauth.socialaccount.providers.orcid',
    'allauth.socialaccount.providers.patreon',
    'allauth.socialaccount.providers.paypal',
    'allauth.socialaccount.providers.persona',
    'allauth.socialaccount.providers.pinterest',
    'allauth.socialaccount.providers.pocket',
    'allauth.socialaccount.providers.quickbooks',
    'allauth.socialaccount.providers.reddit',
    'allauth.socialaccount.providers.robinhood',
    'allauth.socialaccount.providers.salesforce',
    'allauth.socialaccount.providers.sharefile',
    'allauth.socialaccount.providers.shopify',
    'allauth.socialaccount.providers.slack',
    'allauth.socialaccount.providers.snapchat',
    'allauth.socialaccount.providers.soundcloud',
    'allauth.socialaccount.providers.spotify',
    'allauth.socialaccount.providers.stackexchange',
    'allauth.socialaccount.providers.steam',
    'allauth.socialaccount.providers.stocktwits',
    'allauth.socialaccount.providers.strava',
    'allauth.socialaccount.providers.stripe',
    'allauth.socialaccount.providers.telegram',
    'allauth.socialaccount.providers.trainingpeaks',
    'allauth.socialaccount.providers.trello',
    'allauth.socialaccount.providers.tumblr',
    'allauth.socialaccount.providers.twentythreeandme',
    'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.twitter_oauth2',
    'allauth.socialaccount.providers.untappd',
    'allauth.socialaccount.providers.vimeo',
    'allauth.socialaccount.providers.vimeo_oauth2',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.wahoo',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.weixin',
    'allauth.socialaccount.providers.windowslive',
    'allauth.socialaccount.providers.xing',
    'allauth.socialaccount.providers.yahoo',
    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.ynab',
    'allauth.socialaccount.providers.zoho',
    'allauth.socialaccount.providers.zoom',
    'allauth.socialaccount.providers.okta',
    'allauth.socialaccount.providers.feishu',
    ...
]

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

Client ID:
551868905468-afspiie229k0936gn1i5ipj8b4s9dmk5.apps.googleusercontent.com

Client secret:
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

urls.py:

urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]

Note that you do not necessarily need the URLs provided by django.contrib.auth.urls. Instead of the URLs login, logout, and password_change (among others), you can use the URLs provided by allauth: account_login, account_logout, account_set_password…

Post-Installation
In your Django root execute the command below to create your database tables:

python manage.py migrate
Now start your server, visit your admin pages (e.g. http://localhost:8000/admin/) and follow these steps:

Add a Site for your domain, matching settings.SITE_ID (django.contrib.sites app).
For each OAuth based provider, either add a SocialApp (socialaccount app) containing the required client credentials, or, make sure that these are configured via the SOCIALACCOUNT_PROVIDERS[<provider>]['APP'] setting (see example above).



Google
The Google provider is OAuth2 based.

More info:
https://developers.google.com/identity/protocols/OAuth2
App registration
Create a google app to obtain a key and secret through the developer console.

Google Developer Console
https://console.developers.google.com/
After you create a project you will have to create a “Client ID” and fill in some project details for the consent form that will be presented to the client.

Under “APIs & auth” go to “Credentials” and create a new Client ID. Probably you will want a “Web application” Client ID. Provide your domain name or test domain name in “Authorized JavaScript origins”. Finally fill in http://127.0.0.1:8000/accounts/google/login/callback/ in the “Authorized redirect URI” field. You can fill multiple URLs, one for each test domain. After creating the Client ID you will find all details for the Django configuration on this page.

Users that login using the app will be presented a consent form. For this to work additional information is required. Under “APIs & auth” go to “Consent screen” and at least provide an email and product name.

Django configuration
The app credentials are configured for your Django installation via the admin interface. Create a new socialapp through /admin/socialaccount/socialapp/.

Fill in the form as follows:

Provider, “Google”
Name, your pick, suggest “Google”
Client id, is called “Client ID” by Google
Secret key, is called “Client secret” by Google
Key, is not needed, leave blank.
Optionally, you can specify the scope to use as follows:

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

By default (if you do not specify SCOPE), profile scope is requested, and optionally email scope depending on whether or not SOCIALACCOUNT_QUERY_EMAIL is enabled.

You must set AUTH_PARAMS['access_type'] to offline in order to receive a refresh token on first login and on reauthentication requests (which is needed to refresh authentication tokens in the background, without involving the user’s browser). When unspecified, Google defaults to online.




#### Create a new Django project and app
<!-- First, create a new Django project and app using the following command: -->
django-admin startproject google_login
cd google_login
python manage.py startapp accounts

#### Create a new project on Google Developers Console
Go to the Google Developers Console website and create a new project. 
After creating the project, enable the Google+ API 
and create OAuth credentials for the project.

#### Install required packages
<!-- Install the required packages using the following command: -->
pip install google-auth google-auth-oauthlib google-auth-httplib2

#### Configure settings.py
<!-- In your project's settings.py file, add the following lines: -->
INSTALLED_APPS = [
    ...
    'accounts',
    'social_django',
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<Google OAuth2 client ID>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<Google OAuth2 client secret>'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = 'logout'

Replace <Google OAuth2 client ID> and <Google OAuth2 client secret> with the client ID and client secret from the Google Developers Console.

#### Configure urls.py
<!-- In your app's urls.py file, add the following lines: -->
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('social_django.urls', namespace='social')),
]

#### Create templates
Create a login.html template in the accounts/templates/accounts/ 
directory with the following code:

{% extends 'base.html' %}

{% block content %}
<h2>Login with Google</h2>
<a href="{% url 'social:begin' 'google-oauth2' %}" class="btn btn-primary">Login with Google</a>
{% endblock %}

#### Run migrations
<!-- Run the following commands to create the necessary database tables: -->
python manage.py makemigrations
python manage.py migrate

#### Start the development server
<!-- Start the development server using the following command: -->
python manage.py runserver

Now, when you visit http://localhost:8000/login/, you should see a button that allows you to log in with Google. After clicking the button and authenticating with Google, you will be redirected to the home page.

That's it! You have now implemented Google login authentication in your Django project.


# settings.py

import os

# ...

# Google OAuth2 settings
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')



I apologize for the confusion in my previous response. The code snippets for LoginView and LogoutView functions are not included as they are provided by Django's built-in auth_views.

Here's a quick breakdown of what's happening in those lines of code:

LoginView is a built-in Django view that renders a login form and handles authentication.
The template_name argument specifies the path to the login template, which will be used to render the form.
LogoutView is another built-in view that logs out the user and redirects them to a specified page (usually the homepage).
Here's an example of what the views and urls might look like for a simple Django app using Google OAuth2 for authentication:

python
Copy code
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
import json

def google_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        redirect_uri = request.build_absolute_uri('/google-auth/')
        params = {
            'redirect_uri': redirect_uri,
            'response_type': 'code',
            'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
            'scope': 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email'
        }
        url = 'https://accounts.google.com/o/oauth2/auth?' + urlencode(params)
        return redirect(url)

def google_auth(request):
    if request.GET.get('error'):
        return redirect('login')
    else:
        code = request.GET.get('code')
        redirect_uri = request.build_absolute_uri('/google-auth/')
        data = {
            'code': code,
            'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
            'client_secret': settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code'
        }
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post('https://accounts.google.com/o/oauth2/token', data=data, headers=headers)
        access_token = json.loads(response.text)['access_token']
        headers = {'Authorization': 'Bearer ' + access_token}
        response = requests.get('https://www.googleapis.com/oauth2/v1/userinfo', headers=headers)
        google_user = json.loads(response.text)
        try:
            user = User.objects.get(email=google_user['email'])
        except User.DoesNotExist:
            user = User(email=google_user['email'], first_name=google_user['given_name'], last_name=google_user['family_name'])
            user.set_unusable_password()
            user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('home')

@login_required
def home(request):
    return render(request, 'accounts/home.html')

# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('google-login/', views.google_login, name='google-login'),
    path('google-auth/', views.google_auth, name='google-auth'),
    path('home/', views.home, name='home'),
]

In the views.py file, we define a google_login() function that redirects the user to the Google OAuth2 authentication page. This function generates a URL that includes the necessary parameters for initiating the OAuth2 flow.







