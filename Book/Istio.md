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

- Benefit of Virtual services:
	-  địa chỉ nhiều service thông qua duy nhất một virtual serivce

# Terminology
## Host :
Host là một logical network application
## Downstream :
Host connect tới Envoy, gửi request, nhận response.
## Upstream :
Nhận connections và request từ Envoy và return response.
## Listener :
Tên network location(port, unix domain socket, etc) có thể được connected bởi downstream clients. Envoy expose một hoặc nhiều listener để cho downstream host connect tới.
## Cluster :
Là một group logic giống nhau mà upstream host mà Envoy connect tới. Envoy discovers member của cluster thông qua serivce discovery.

## Mesh
 A group of hosts that coordinate to provide a consistent network topology. In this documentation, an “Envoy mesh” is a group of Envoy proxies that form a message passing substrate for a distributed system comprised of many different services and application platforms.
## Runtime configuration
 Out of band realtime configuration system deployed alongside Envoy. Configuration settings can be altered that will affect operation without needing to restart Envoy or change the primary configuration.
# Architecture overview
## Listener

# Traffice Management
## Virtual Services
Nếu không xài thằng này, Envoy sẽ phân phối traffic bằng cách dùng round-robin loadbalancing giữa các endpoints của services. Bạn có thể routing traffice nếu các deployment có phiên bản khác nhau.
Túm cái váy lại Virtual Services cho phép chúng ta:
- Giải quyết nhiều services thông qua duy nhất một virtual services. Ví dụ, chúng ta có thể config virtual service để handle tất cả các services trong một namespace. 
- Config luật traffic với **GateWay** để control ingress và egress.
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
  - reviews
  http:
  - match:
    - headers:
        end-user:
          exact: jason
    route:
    - destination:
        host: reviews
        subset: v2
  - route:
    - destination:
        host: reviews
        subset: v3
```
> Còn một số config nữa tuy nhiên hiểu nôm na nó là thế là được rồi :wink: :wink:

## Destination Rule
Nếu virtual services là cách mà chúng ta route traffic, thì destination rule là config để chuyện gì sẽ xảy ra tại destination.
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: my-destination-rule
spec:
  host: my-svc
  trafficPolicy:
    loadBalancer:
      simple: RANDOM
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
    trafficPolicy:
      loadBalancer:
        simple: ROUND_ROBIN
  - name: v3
    labels:
      version: v3
```
## Gateways
Để quản lý inbound và outbound traffic cho service mesh. Để specify traffic nào đưa ra vô mesh. Gateways config được app
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg0Nzk2NDk4LDc4MDc2NDAyNSwxNzA1OT
IwMzgxLC0yNjg5NTM1MjMsLTQ2MTAyNTI1OCwxNzExMjE1NjQ1
LDgyNjIzMjI0NiwxNzM4MjA2MTIsODk1ODAwOTAzLDE1ODc3Mz
g1ODgsMzQ0MjI4NzMyLDIwMDA1NzA0NjEsMTE5MTQ0MDUxLDY5
OTQ3MDU3NCwtMTg2MjIzMDk4NF19
-->