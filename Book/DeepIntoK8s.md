# Networking K8S on AWS
## Introduction K8S Pod Networking
### Kubernetes Container Network Interface (CNI) :smile:
![cni-plugin.png](https://images.contentstack.io/v3/assets/blt300387d93dabf50e/blt605e7720be3d37fd/5bf6f4bcc812d64628f03c5b/cni-plugin.png)
- Pods trong K8s cluster chia sẻ 1 địa chỉ IP
- Containers trong K8s cluster nhìn thấy cùng 1 địa chỉ IP cho chính chúng như các pods khác (và node) để tiếp cận container đó.
- Nếu không có network policies, tất cả các pods và node có thể giao tiếp với từng loại một cách thoại mái, without NAT
## Network Policy
# Note
[https://medium.com/@AADota/kubernetes-liveness-and-readiness-probes-difference-1b659c369e17#:~:text=Summary,our%20application%20from%20serving%20traffic.](https://medium.com/@AADota/kubernetes-liveness-and-readiness-probes-difference-1b659c369e17#:~:text=Summary,our%20application%20from%20serving%20traffic.)

## Service
Example:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```
- Tạo một service object gọi là _my-serivce_
- Kube cấp cho Service đó một địa chỉ IP(ClusterIP), được dùng bởi Service proxies.
- **Note:** A Service can map _any_ incoming `port` to a `targetPort`. By default and for convenience, the `targetPort` is set to the same value as the `port` field.

####
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjE1MTgyNTkwLC0xNTUzOTkwNjg2LDMzOD
E0MTIyOSwtMTU1Njk1NzAwNiwxMzE4MzcxMzMxXX0=
-->