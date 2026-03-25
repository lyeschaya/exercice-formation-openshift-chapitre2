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
- Namespace : `formation-openshift`

## Instructions

### Étape 1 — Créer le fichier job.yaml

Créez un fichier `job.yaml` dans votre dossier de travail.

**Indices :**
- Kind : `Job`
- apiVersion : `batch/v1`
- Nom du job : `demo-job-3`
- Image : `nginxinc/nginx-unprivileged`
- La commande doit afficher un message avec `echo`
- Le pod ne doit pas redémarrer en cas d'échec (`restartPolicy: Never`)

### Étape 2 — Appliquer le Job
```bash
oc apply -f job.yaml -n formation-openshift
```

### Étape 3 — Vérifier le Job

**Indices :**
- Utilisez `oc get jobs` pour voir le statut
- Le statut attendu est `Complete`

### Étape 4 — Voir les logs du Job

**Indices :**
- Utilisez `oc logs job/<nom-du-job>` pour voir les logs
- Vous devriez voir le message affiché par la commande `echo`

### Étape 5 — Créer le fichier cronjob.yaml

Créez un fichier `cronjob.yaml` dans votre dossier de travail.

**Indices :**
- Kind : `CronJob`
- apiVersion : `batch/v1`
- Nom : `demo-cronjob-3`
- Image : `nginxinc/nginx-unprivileged`
- Schedule : toutes les minutes (`*/1 * * * *`)
- La commande doit afficher un message avec `echo`
- Le pod ne doit pas redémarrer (`restartPolicy: Never`)
- **Important** : Pour ne pas consommer trop de ressources, limitez l'historique :
  - `successfulJobsHistoryLimit: 3` → garde seulement les 3 derniers jobs réussis
  - `failedJobsHistoryLimit: 1` → garde seulement le dernier job échoué

### Étape 6 — Appliquer le CronJob
```bash
oc apply -f cronjob.yaml -n formation-openshift
```

### Étape 7 — Vérifier le CronJob

**Indices :**
- Utilisez `oc get cronjob` pour voir le schedule
- Attendez 1 minute et utilisez `oc get jobs` pour voir les jobs créés automatiquement

### Étape 8 — Tester manuellement le CronJob

Sans attendre le schedule, déclenchez manuellement le CronJob.

**Indices :**
- Utilisez `oc create job` avec l'option `--from=cronjob/<nom>`
- Vérifiez les logs du job créé

### Étape 9 — Tester depuis la console OpenShift

Pour le Job :
1. Allez dans **Workloads** → **Jobs**
2. Cliquez sur le job → onglet **Logs**
3. Vous devriez voir le message affiché par la commande `echo`

Pour le CronJob :
1. Allez dans **Workloads** → **CronJobs**
2. Cliquez sur le CronJob → onglet **Jobs**
3. Attendez 1 minute → un nouveau Job apparaît automatiquement

## Résultat attendu
- Le Job est en status `Complete`
- Le CronJob s'exécute toutes les minutes automatiquement
- L'historique est limité à 3 jobs réussis et 1 job échoué
- Les logs affichent le message attendu

## Bloqué ?
Consultez le dossier `solution/` ou l'app ArgoCD `formation-exercice-3`.
