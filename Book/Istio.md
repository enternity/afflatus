# Config certificate

```
istioctl x create-remote-secret --context=${REMOTE_CLUSTER_CTX} --name ${REMOTE_CLUSTER_NAME} | kubectl apply -f - --context=${MAIN_CLUSTER_CTX}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjk5NDcwNTc0LC0xODYyMjMwOTg0XX0=
-->