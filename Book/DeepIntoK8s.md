# Networking K8S on AWS
## Introduction K8S Pod Networking
### Kubernetes Container Network Interface (CNI) :smile:
![cni-plugin.png](https://images.contentstack.io/v3/assets/blt300387d93dabf50e/blt605e7720be3d37fd/5bf6f4bcc812d64628f03c5b/cni-plugin.png)
- Pods trong K8s cluster chia sẻ 1 địa chỉ IP
- Containers trong K8s cluster nhìn thấy cùng 1 địa chỉ IP cho chính chúng như các pods khác (và node) để tiếp cận container đó.
- Nếu không có network policies, tất cả các pods và node có thể giao tiếp với từng loại một cách thoại mái, without NAT
## Network Policy

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NTY5NTcwMDYsMTMxODM3MTMzMV19
-->