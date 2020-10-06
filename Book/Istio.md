[https://blog.jayway.com/2018/10/22/understanding-istio-ingress-gateway-in-kubernetes/#:~:text=Traditionally%2C%20Kubernetes%20has%20used%20an,new%20Gateway%20and%20VirtualServices%20resources.](https://blog.jayway.com/2018/10/22/understanding-istio-ingress-gateway-in-kubernetes/#:~:text=Traditionally%2C%20Kubernetes%20has%20used%20an,new%20Gateway%20and%20VirtualServices%20resources.)
# Chú 
# Config certificate

```
istioctl x create-remote-secret --context=${REMOTE_CLUSTER_CTX} --name ${REMOTE_CLUSTER_NAME} | kubectl apply -f - --context=${MAIN_CLUSTER_CTX}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA3OTMzOTgwMSwxMTkxNDQwNTEsNjk5ND
cwNTc0LC0xODYyMjMwOTg0XX0=
-->