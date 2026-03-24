# Exercice 1 — Déploiement nginx simple

## Objectif
Déployer nginx sur OpenShift manuellement.

## Ce que tu dois faire

1. Créer un Deployment nginx-unprivileged
   - Image : nginxinc/nginx-unprivileged
   - Replicas : 3
   - Port : 8080

2. Créer un Service
   - Port : 8080

3. Créer une Route OpenShift

4. Namespace : exercice-nginx-1

## Commandes utiles
```bash
# Créer le namespace
oc new-project exercice-nginx-1

# Appliquer les fichiers
oc apply -f deployment.yaml
oc apply -f service.yaml
oc apply -f route.yaml

# Vérifier
oc get pods -n exercice-nginx-1
oc get route -n exercice-nginx-1
```

## Si tu bloques
Regarde le dossier `solution/` ou ArgoCD app `nginx-exercice-1-solution`
