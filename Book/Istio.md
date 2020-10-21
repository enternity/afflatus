[https://blog.jayway.com/2018/10/22/understanding-istio-ingress-gateway-in-kubernetes/#:~:text=Traditionally%2C%20Kubernetes%20has%20used%20an,new%20Gateway%20and%20VirtualServices%20resources.](https://blog.jayway.com/2018/10/22/understanding-istio-ingress-gateway-in-kubernetes/#:~:text=Traditionally%2C%20Kubernetes%20has%20used%20an,new%20Gateway%20and%20VirtualServices%20resources.)
# Chú ý : resource khi start cluster (không thì không đủ để inject istio vô :grinning: :wink: :heart:)
# Config certificate

```
istioctl x create-remote-secret --context=${REMOTE_CLUSTER_CTX} --name ${REMOTE_CLUSTER_NAME} | kubectl apply -f - --context=${MAIN_CLUSTER_CTX}
```
# Traffic management
## Virtual Services
- Nếu không xài virtual services thì **Envoy distributed** route traffic bằng cách dùng roundrobin. Tuy nhiên muốn route traffic bao nhiêu % vô instance nào thì dùng ông nội này.

Example :
A typical use case is to send traffic to different versions of a service, specified as service subsets. Clients send requests to the virtual service host as if it was a single entity, and Envoy then routes the traffic to the different versions depending on the virtual service rules: for example, “20% of calls go to the new version” or “calls from these users go to version 2”. This allows you to, for instance, create a canary rollout where you gradually increase the percentage of traffic that’s sent to a new service version. The traffic routing is completely separate from the instance deployment, meaning that the number of instances implementing the new service version can scale up and down based on traffic load without referring to traffic routing at all. By contrast, container orchestration platforms like Kubernetes only support traffic distribution based on instance scaling, which quickly becomes complex. You can read more about how virtual services help with canary deployments in [Canary Deployments using Istio](https://istio.io/latest/blog/2017/0.1-canary/).

- Benefi
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3ODgzNTAyMTksMjAwMDU3MDQ2MSwxMT
kxNDQwNTEsNjk5NDcwNTc0LC0xODYyMjMwOTg0XX0=
-->