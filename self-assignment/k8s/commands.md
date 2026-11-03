# Self-Assignment 15-17 (Kubernetes)
```bash
# Q15 Pod
kubectl apply -f nginx-pod.yaml
kubectl get pods
kubectl port-forward pod/nginx-pod 8080:80      # browser: http://localhost:8080  (Ctrl+C to stop)
# Q16 Deployment with 5 replicas
kubectl apply -f nginx-deployment.yaml
kubectl get pods
kubectl delete pod <any-nginx-deploy-pod>; kubectl get pods     # replacement created
# Q17 Service
kubectl apply -f nginx-service.yaml
kubectl get svc nginx-svc
minikube service nginx-svc --url                # open the printed URL
kubectl get endpoints nginx-svc                 # lists the pod IPs receiving traffic
```
