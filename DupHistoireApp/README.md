# DupHistoire - Application Android Éducative

![Langage](https://img.shields.io/badge/langage-Kotlin-blueviolet)
![UI](https://img.shields.io/badge/UI-Jetpack%20Compose-blue)
![API](https://img.shields.io/badge/API-24%2B-brightgreen)

**DupHistoire** est une application Android native conçue pour présenter de manière simple et accessible des contenus historiques sur le rôle des enfants durant la Seconde Guerre mondiale.

L'application sert de visionneuse pour une série d'articles pédagogiques, offrant une expérience de lecture focalisée et sans distraction, idéale pour un projet scolaire ou de sensibilisation.

## 📜 Contenu

L'application aborde plusieurs thèmes importants à travers des articles dédiés :
*   Le quotidien des enfants français et allemands pendant la guerre.
*   Le rôle crucial des enfants dans la Résistance.
*   Le sort des enfants pendant la Shoah.
*   La vie des "enfants maudits" après la guerre.

Le contenu est basé sur les articles du site [German History](https://sites.google.com/view/duphistoire).

## ✨ Fonctionnalités

*   **Interface Simple** : Une application mono-activité qui affiche le contenu web localement.
*   **Contenu Embarqué** : Les articles sont stockés localement dans l'application pour un accès hors-ligne.
*   **Navigation Facile** : Conçue pour une lecture simple et directe du contenu historique.

## 🛠️ Technologies et Architecture

*   **Langage** : 100% [Kotlin](https://kotlinlang.org/).
*   **Interface Utilisateur** : Entièrement construite avec [Jetpack Compose](https://developer.android.com/jetpack/compose), le toolkit moderne de Google pour les UI natives Android.
*   **Architecture** : Application simple suivant les principes de base d'Android (Activity, WebView).
*   **Build System** : [Gradle](https://gradle.org) avec le DSL Kotlin (`build.gradle.kts`).

## 👨‍💻 Pour les Développeurs

### Prérequis
*   [Android Studio](https://developer.android.com/studio) (dernière version recommandée)
*   JDK 11 ou supérieur

### Installation
1.  Clonez ce dépôt :
    ```bash
    git clone [URL_DU_DEPOT]
    cd DupHistoireApp
    ```
2.  Ouvrez le projet avec Android Studio.
3.  Laissez Gradle synchroniser les dépendances.
4.  Lancez l'application sur un émulateur ou un appareil physique.

### Structure du Projet
```
DupHistoireApp/
├── app/
│   ├── src/main/
│   │   ├── java/com/example/duphistoire/  # Code source Kotlin
│   │   ├── AndroidManifest.xml            # Manifeste de l'application
│   └── build.gradle.kts                   # Configuration du module 'app'
├── gradle/                                # Wrapper Gradle
└── build.gradle.kts                       # Configuration du projet racine
```

## 🤝 Contribution

Ce projet étant principalement une visionneuse de contenu statique, les contributions peuvent se concentrer sur :
*   L'amélioration de l'interface utilisateur (UI/UX).
*   L'ajout de fonctionnalités (ex: quiz, recherche, favoris).
*   La mise à jour du contenu historique.

N'hésitez pas à forker le projet et à proposer des Pull Requests.

## 📄 Licence
Ce projet n'a pas de licence définie. Pour un projet open-source, je vous suggère d'ajouter une licence comme [MIT](https://opensource.org/licenses/MIT) ou [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html).
