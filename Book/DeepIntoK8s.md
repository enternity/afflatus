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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA2OTgxMDQ1NiwtMTU1Njk1NzAwNiwxMz
E4MzcxMzMxXX0=
-->