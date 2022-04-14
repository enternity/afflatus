[https://learnk8s.io/kubernetes-long-lived-connections](https://learnk8s.io/kubernetes-long-lived-connections)
[https://blog.twitter.com/engineering/en_us/topics/infrastructure/2019/daperture-load-balancer.html](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2019/daperture-load-balancer.html)
[https://scalingo.com/blog/iptables#load-balancing](https://scalingo.com/blog/iptables#load-balancing)
[service-mesh](https://medium.com/vinid/c%C6%A1-b%E1%BA%A3n-service-mesh-istio-cho-ng%C6%B0%E1%BB%9Di-m%E1%BB%9Bi-b%E1%BA%AFt-%C4%91%E1%BA%A7u-3563b582ed51)
[https://platform9.com/blog/kubernetes-service-mesh-a-comparison-of-istio-linkerd-and-consul/](https://platform9.com/blog/kubernetes-service-mesh-a-comparison-of-istio-linkerd-and-consul/)
- Nếu có 3 IP cùng phục vụ một service thì kube-proxy sẽ thực hiện theo luật như sau
1. Lấy pod 1 với xác suất 33%, nếu không thì bước 2.
2. Lấy pod 2 với xác suất 50%. Nếu không thì bước 3.
3. Lấy pod 3 (lựa chọn cuối cùng)

![iptables rules for three Pods](https://learnk8s.io/a/851d04da950f1e7db3e460ba902c0ede.svg)

**IPTables** dùng [statistic module]([http://ipset.netfilter.org/iptables-extensions.man.html#lbCD](http://ipset.netfilter.org/iptables-extensions.man.html#lbCD)) nên load balance ở đây là random


[https://blog.envoyproxy.io/introduction-to-modern-network-load-balancing-and-proxying-a57f6ff80236](https://blog.envoyproxy.io/introduction-to-modern-network-load-balancing-and-proxying-a57f6ff80236)

[https://medium.com/google-cloud/kubernetes-autoscaling-with-istio-metrics-76442253a45a](https://medium.com/google-cloud/kubernetes-autoscaling-with-istio-metrics-76442253a45a)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MTY0OTMxNDldfQ==
-->