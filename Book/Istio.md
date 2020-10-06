
# Config certificate

```
istioctl x create-remote-secret --context=${REMOTE_CLUSTER_CTX} --name ${REMOTE_CLUSTER_NAME} | kubectl apply -f - --context=${MAIN_CLUSTER_CTX}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDM4NzQwNjM2LDY5OTQ3MDU3NCwtMTg2Mj
IzMDk4NF19
-->