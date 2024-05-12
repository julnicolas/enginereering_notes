# File Rights
File rights can be modified with the `chmod` command.

They are set by giving a set of 4 octal values of the form `abcd`. Where:
- `a`: is the special, `sticky bit` section, discussed later
- `b`: the permissions for the owning user
- `c`: the permissions for the owning group
- `d`: the permissions for the rest

Every permission on operations are represented by an octal value:
- `4`: read
- `2`: write
- `1`: execute
- `0`: not permitted

They can be combined, using a sum. Hence the `read and wright` permission
works out to `6`.

The `740` therefore gives:
- read, write and execution permission for the owner
- read-only permission for the owning group
- no permissions at all for the rest

When not provided, the leading `4th` digit is set to 0 (the sticky bit).
Therefore, 0740 == 740.

## The sticky bit section
The sticky bit section is the leading digit of the four-digit-value setting
permissions. It has the following meaning:
- `4`: `setuid` mode
- `2`: `setguid` mode
- `1`: `sticky` mode
- `0`: no special permission granted

Here is a detailed description.


### SETUID

Ce premier « droit » spécial ne s’applique qu’à
des fichiers et pas des répertoires. Son utilisation est la plus 
simple à appréhender. Il faut d’abord comprendre le fait 
que quand un utilisateur exécute un script ou un lance un binaire 
quelconque, celui-ci se lance avec les droits de cet 
utilisateur. Par conséquent, et en fonction de ce que le 
script fait, il se peut que certaines actions ne soient pas 
permises avec le niveau de droits de l’utilisateur (par 
exemple écrire dans des fichiers appartenant à root). L’exemple 
le plus courant est l’utilisation de la commande passwd. 
Lorsqu’on souhaite changer son mot de passe, c’est 
cette commande qu’on utilise. Mais pour que le changement 
de mot de passe soit effectif, il faut que passwd puisse 
écrire dans les fichiers. /etc/passwd et /etc
/shadow. Problème, en tant qu’utilisateur nous n’avons 
pas le droit d’écrire dans ces fichiers. C’
est là que SETUID entre en action. On dit alors que 
passwd est « setuidé » Celà veut dire que passwd est lancé 
avec les droits de root et du coup en tant qu’utilisateur 
l’écriture dans les fichiers précédemment cités est donc possible. 

Voici comment apparaît le SETUID :
``` sh
-rwsr-
xr-x 1 root root 59640 Sep 27 2017 /usr/bin/passwd*
```

Notez le s à la place du x pour le groupe de 
permissions du propriétaire (ici root). Sa valeur octale est 4.
Les droits de passwd sont donc 4755

Pour positionner le SETUID il existe 2 méthodes, identiques à celles 
que nous avons vues au-dessus :
``` sh
chmod 4755 
```
qui donne les droits vus sur passwd. soit
``` sh
chmod u+s
```

### SETGID

Contrairement à SETUID, SETGID,  s’applique aussi bien aux 
fichiers qu’aux répertoires. Pour les fichiers, l’application 
et le comportement sont les mêmes. A savoir qu’un 
utilisateur qui lancerait un script ou un binaire, lui appartenant 
mais qui serait « setguidé » s’exécuterait avec les droits 
du groupe auquel il appartient. Ainsi un script « setgidé » 
« root » par exemple, pourrait écrire/lire dans des 
fichiers ou répertoires inaccessibles à l’utilisateur en temps normal.

En revanche quand un répertoire est «setgidé », le comportement observé 
change. On ne parle alors plus de droits d’exécution 
mais d’appartenance. En effet, tous les fichiers ou 
sous-répertoires qui seraient créés dans un tel répertoire, appartiendraient 
automatiquement au groupe auquel appartient le dossier. Si plusieurs utilisateurs peuvent 
et/ou doivent travailler dans un même répertoire par exemple, 
on peut positionner le droit SETGID sur ce répertoire afin que tous 
les utilisateurs puissent accéder à son contenu sans restrictions liées au propriétaire 
qui a créé le fichier ou le sous-répertoire. C’est une solution bien plus élégante 
que de faire un horrible chmod 777 ! Voici comment apparaît le SETGID :

``` sh
drwxr-sr-x 2 julien julien 4096 Jun 3 13:03 test/
```

Notez le s à la place du x pour le groupe de 
permissions du groupe (ici julien). Sa valeur octale est 2. 
Les droits de test sont donc 2755

Pour positionner le SETGID il existe 2 méthodes, identiques à celles 
que nous avons vues au-dessus :
``` sh
chmod 2755
```
qui donne les droits vus sur test/ soit
``` sh
chmod g+s
```

### STICKY BIT

Tout comme SETGID, le STICKY BIT peut s’appliquer aussi 
bien aux fichiers (et donc aux binaires/scripts) qu’aux 
répertoires. Lorsqu’il est positionné sur un fichier,
 celà permet à l’exéctuble de rester en mémoire même 
si le programme qui l’invoque est terminé, (d’où le 
terme sticky pour collant en anglais). Cette fonctionnalité 
était très utilisée sur les systèmes Unix dans les années 70/80
car il fallait du temps à l’époque pour charger 
un exécutable en mémoire et le rendre disponible à l’utilisation. 
Du coup positionner le STICKY BIT permettait au système de garder 
cet exécutable en swap pour le charger plus rapidement en mémoire par 
la suite. Avec la puissance des ordinateurs actuels et les vitesses 
de bus mémoire, cette méthode n’est quasiment plus utilisée.

En revance pour les répertoires il est toujours très utile. Postionné 
sur un dossier, le STICKY BIT permet d’interdire la 
suppression du répertoire et/ou de son contenu par quiconque n’en est 
pas propriétaire. L’exemple le plus parlant pour démontrer celà est 
le cas du répertoire /tmp. N’importe quel utilisateur 
du système peut créer ou supprimer des fichiers ou des dossiers dans 
/tmp, mais il le pourra pas supprimer ceux créés par 
quelqu’un d’autre. Ceci est permis grâce au 
positionnement du STICKY BIT. Voici comment il apparaît :

``` sh
drwxrwxrwt 28 root root 12288 Jun 4 10:16 tmp/
```

Notez le t à la fin à la place du x pour 
le groupe de permissions des autres. Sa valeur octale est 1. 
Les droits de /tmp sont donc 1777

A noter que si les droits d’exécution sont positionnés le t devient T.

Pour positionner le STICKY BIT il existe 2 méthodes, identiques à 
celles que nous avons vues au-dessus :

``` sh
chmod 1777
```
qui donne les droits vus sur test/ soit

``` sh
chmod o+t
```

