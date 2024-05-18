# MonEtflix
[Visiter](http://cinema.raspi)

[Admin site](http://cinema.raspi/admin)
Username: admin
Password: admin

## Prerequis
1. Ajouter 192.168.1.16 au dns pour acceder au site web

2. Avoir une façon de modifier le code
- [git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)
- editeur de code

## Possibilitées Prerequis
- tester un editeur de code en ligne et ne pas utiliser git
- Utiliser WSL (windows subsytem for linux)

## TODO

### Backend

- [ ] Refactoriser les views
- [ ] Améliorer le script pour scrap les web avec des films pour avoir plus de sources

#### Genre

- [ ] Un film peut avoir +1 genre (But: Design de base de données)
- [ ] Ajouter tous les genres dans la navbar [tip](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/#adding-extra-context)
 
#### Person

- [ ] Une personne peut etre un acteur ou un realisateur (But: Pratique object oriented programming + bonne pratiques de développement)
- [ ] Ajouter plus de details sur les acteurs et directeurs

#### Movie

- [ ] Si un film fait partie d'une saga on veut connaitre l'ordre et pouvoir regarder le suivant ou l'anterieur
- [ ] On veut connaitre la note du film
- [ ] On veut connaitre le réalisatuer/producteur du film
- [ ] On veut plus d'informations sur les films (But: Data engineering + Hacking)

- [ ] On veut pouvoir noter les films
- [ ] On veut un historique des films regardé (But: Création et gestion d'utilisateurs)
- [ ] On veut enregistrer des favoris

- [ ] On veut des filtres plus complex afin de mieux trouver des films (But: Design de base de données + REST API endpoints)

- [ ] Avoir plusieures sources pour regarder les films
- [ ] Avoir une façon de savoir si une source est toujours active

#### Saga

- [ ] On veut voir les saga

#### Series

- [ ] On veut ajouter des series et avoir les mêmes capabilitées que les films (But: Pratique object oriented programming + bonne pratiques de développement)

### Frontend

- [ ] On veut améliorer l'interface (But: UI/UX design)

## Docker

### Build
```bash
docker build -t cinema .
```

### Run
```bash
docker run -d -p 8001:8001 --name cinema cinema
```
