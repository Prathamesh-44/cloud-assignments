# Assignment 6 - Kubernetes (minikube)
```bash
minikube start --driver=docker
alias kubectl="minikube kubectl --"      # per course slides; or install kubectl normally
```
## Pods (Q1-6)
```bash
kubectl run web1 --image=nginx                 # Q1
kubectl get pods                               # Q2
kubectl describe pod web1                      # Q3
kubectl logs web1                              # Q4
kubectl delete pod web1; kubectl get pods      # Q5
kubectl run web2 --image=httpd                 # Q6
```
## ReplicaSet (Q7-11) - kubectl cannot create a ReplicaSet directly, so apply YAML
```bash
kubectl apply -f replicaset.yaml               # Q7
kubectl get rs; kubectl get pods               # Q8
kubectl delete pod <one-web-rs-pod-name>; kubectl get pods    # Q9: new pod appears
kubectl scale rs web-rs --replicas=5           # Q10
kubectl scale rs web-rs --replicas=2           # Q11
```
## Deployment (Q12-15, 19, 20)
```bash
kubectl create deployment web-deploy --image=nginx --replicas=3     # Q12
kubectl get deploy,rs,pods                                          # Q13
kubectl scale deploy web-deploy --replicas=5                        # Q14
kubectl set image deployment/web-deploy nginx=httpd                 # Q15 (container is named "nginx")
kubectl rollout status deployment/web-deploy
kubectl delete pod <web-deploy-pod>; kubectl get pods               # Q19
kubectl delete deploy web-deploy; kubectl get deploy,rs,pods        # Q20: all gone
```
## Failures (Q16-18)
```bash
kubectl run crash1 --image=busybox --restart=Always -- sh -c "exit 1"
kubectl get pods -w                    # STATUS: Error -> CrashLoopBackOff, RESTARTS climbs
kubectl run crash2 --image=busybox --restart=Always -- sh -c "sleep 5; exit 1"
kubectl get pods -w                    # Running -> Error -> CrashLoopBackOff
kubectl run bad --image=nginx-invalid
kubectl get pods                       # ErrImagePull -> ImagePullBackOff
kubectl describe pod bad               # see Events section
```
