[https://learnk8s.io/kubernetes-long-lived-connections](https://learnk8s.io/kubernetes-long-lived-connections)
[https://blog.twitter.com/engineering/en_us/topics/infrastructure/2019/daperture-load-balancer.html](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2019/daperture-load-balancer.html)
[https://scalingo.com/blog/iptables#load-balancing](https://scalingo.com/blog/iptables#load-balancing)
- Nếu có 3 IP cùng phục vụ một service thì kube-proxy sẽ thực hiện theo luật như sau
1. Lấy pod 1 với xác suất 33%, nếu không thì bước 2.
2. Lấy pod 2 với xác suất 50%. Nếu không thì bước 3.
3. Lấy pod 3 (lựa chọn cuối cùng)

![iptables rules for three Pods](https://learnk8s.io/a/851d04da950f1e7db3e460ba902c0ede.svg)

**IPTables** dùng [statistic module]([http://ipset.netfilter.org/iptables-extensions.man.html#lbCD](http://ipset.netfilter.org/iptables-extensions.man.html#lbCD)) nên load balance ở đây là random
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MTkwMDYwMiwxOTY3Nzc0MzI0XX0=
-->