[https://blog.jayway.com/2018/10/22/understanding-istio-ingress-gateway-in-kubernetes/#:~:text=Traditionally%2C%20Kubernetes%20has%20used%20an,new%20Gateway%20and%20VirtualServices%20resources.](https://blog.jayway.com/2018/10/22/understanding-istio-ingress-gateway-in-kubernetes/#:~:text=Traditionally%2C%20Kubernetes%20has%20used%20an,new%20Gateway%20and%20VirtualServices%20resources.)
# Chú ý : resource khi start cluster (không thì không đủ để inject istio vô :grinning: :wink: :heart:)
# Config certificate

```
istioctl x create-remote-secret --context=${REMOTE_CLUSTER_CTX} --name ${REMOTE_CLUSTER_NAME} | kubectl apply -f - --context=${MAIN_CLUSTER_CTX}
```
# Traffic management

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcwNDc5OTA2MiwyMDAwNTcwNDYxLDExOT
E0NDA1MSw2OTk0NzA1NzQsLTE4NjIyMzA5ODRdfQ==
-->