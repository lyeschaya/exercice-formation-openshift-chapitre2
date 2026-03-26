# Dashboard OpenShift — Job & CronJob

Dashboard interactif Flask connecté à l'API OpenShift.

## Fonctionnalités
- Voir les Jobs et CronJobs en temps réel
- Déclencher un Job ou CronJob manuellement
- Afficher les logs dans un terminal intégré
- Supprimer un job depuis l'interface
- Mode sombre / mode clair

## Limitations
- Max 3 jobs manuels simultanés
- Max 10 jobs total dans le namespace
- Suppression automatique après 5 minutes

## Stack
- Python Flask
- Kubernetes Python SDK
- OpenShift Registry
- ArgoCD GitOps

## URL
https://dashboard-route-formation-openshift.apps.neutron-sno-gpu.neutron-it.fr
