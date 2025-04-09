# 📊 EcomData - Pipeline Big Data

## 📝 Contexte

EcomData est une plateforme e-commerce spécialisée dans la vente de produits électroniques. L’entreprise souhaite centraliser et automatiser la gestion de ses données (commandes et interactions utilisateur) qui sont actuellement dispersées.

---

## 🚧 Problématique

- Données stockées dans différents formats (CSV, JSON) et systèmes.
- Ingestion des données manuelle → erreurs et lenteur.
- Difficile d’analyser les données efficacement.

---

## 🎯 Objectifs

- Générer automatiquement des fichiers de commandes (CSV) et d’interactions utilisateur (JSON).
- Envoyer les fichiers CSV vers **Minio** et les fichiers JSON vers **Kafka** avec **Apache NiFi**.
- Orchestrer le pipeline avec **Apache Airflow**.
- Assurer la conformité au **RGPD** et la qualité des données.

---

## 🛠️ Étapes du Projet

1. **Génération de données (Python)**  
   → Fichiers CSV et JSON enregistrés dans `/Staging`

2. **Ingestion avec Apache NiFi**
   - CSV → Minio (`GetFile → PutS3Object`)
   - JSON → Kafka (`GetFile → PublishKafka`)

3. **Orchestration avec Airflow**
   - Exécution automatique du script Python chaque heure
   - Déclenchement des flux NiFi
   - Vérification de l’envoi des fichiers

---
## 🔐 RGPD & Gouvernance

- Données personnelles protégées.
- Catalogue de données pour assurer traçabilité et qualité.

---

## 🔧 Outils Utilisés

- **Python**
- **Apache NiFi**
- **Apache Airflow**
- **Minio**
- **Kafka**

---

## 👨‍💻 Auteur

Projet réalisé par ALI & IMADE .
