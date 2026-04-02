# Exercice 3 — Job et CronJob

## Contexte

Dans cet exercice, vous allez apprendre à exécuter des tâches ponctuelles et planifiées sur OpenShift avec les ressources Job et CronJob.

- **Job** : exécute une tâche une seule fois jusqu'à completion
- **CronJob** : exécute une tâche de façon planifiée (comme cron Linux)

## Objectifs pédagogiques

- Créer et exécuter un Job OpenShift
- Créer un CronJob avec un schedule défini
- Vérifier les logs d'exécution

## Prérequis

- Avoir complété l'exercice 2
- Être connecté au cluster OpenShift
- Namespace : `formation-openshift`

## Instructions

### Étape 1 — Créer le Job

- Aller dans **Workloads → Jobs**
- Cliquer sur **Create Job**
- Coller le YAML suivant dans l'éditeur :

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: demo-job-console
spec:
  template:
    spec:
      containers:
        - name: job
          image: nginxinc/nginx-unprivileged@sha256:731f382bbad9a874f9f27db9c82d9e671e603e2210386a8e2b6da36cf336fa75
          command: ["sh", "-c", "echo Bonjour depuis mon Job OpenShift"]
      restartPolicy: Never
```

- Cliquer **Create**

### Étape 2 — Vérifier les logs du Job

- Vérifier que le Job est en statut `Complete`
- Cliquer sur **Pods**
- Sélectionner le Pod créé par le Job
- Ouvrir l'onglet **Logs**
- Vous devriez voir : `Bonjour depuis mon Job OpenShift`

### Étape 3 — Créer le CronJob

- Aller dans **Workloads → CronJobs**
- Cliquer sur **Create CronJob**
- Coller le YAML suivant dans l'éditeur :

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: demo-cronjob-console
spec:
  schedule: "*/1 * * * *"
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: cronjob
              image: nginxinc/nginx-unprivileged@sha256:731f382bbad9a874f9f27db9c82d9e671e603e2210386a8e2b6da36cf336fa75
              command: ["sh", "-c", "echo CronJob OpenShift fonctionne"]
          restartPolicy: Never
```

- Cliquer **Create**

### Étape 4 — Vérifier le CronJob

- Aller dans **Workloads → CronJobs**
- Cliquer sur `demo-cronjob-console`
- Cliquer sur l'onglet **Jobs**
- Attendre 1 minute → un nouveau Job apparaît automatiquement
- Cliquer sur un Job → **Pods** → **Logs**
- Vous devriez voir : `CronJob OpenShift fonctionne`

### Étape 5 — Tester manuellement le CronJob

- Aller dans **Workloads → CronJobs**
- Cliquer sur `demo-cronjob-console`
- Cliquer sur **Actions → Create Job**
- Vérifier les logs du Job créé

## Résultat attendu

- Le Job est en statut `Complete`
- Le CronJob s'exécute toutes les minutes automatiquement
- Les logs affichent les messages attendus

## Bloqué ?

Consultez le dossier `solution/` ou demandez à votre formateur de basculer le path ArgoCD vers `nginx-exercice-3/solution`.

