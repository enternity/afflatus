> Bài viết được dịch trên cuốn Mastering Kubernetes - GigiSayfan, hình ảnh cũng được dịch trên cuốn này luôn. Hiểu nôm na chỉ là google trans
# Concepts
## Clusters
- Tập hợp các host lưu trữ và networking resources 
- Các lợi ích :
	- Dễ dùng : không cần lo việc chạy một process quản lý , các signal và exit-code.
	- Tối ưu : Bởi vì infra của k8s chịu nhiều trách nhiệm hơn, nên container càng nhẹ hơn.
## Label :
- Là một key/value được gắn vào các đối tượng, như pods. Labels được dự định dùng để xác thực một số các thuộc tính đặc biệt của đối tượng, có nghĩa và  phù hợp với người dùng nhưng không ngụ ý trực tiếp ngữ nghĩa của lõi của hệ thống. Có t hể dùng để tổ chức và lựa chọn object trong 1 list objects.
## Service : 
Thường được cung cấp các function cho user hoặc service khác. Nó thường bao gồm một group pds, Thường được định danh bởi label. Service được công khai hoặc được phát hiện bởi 1 trong 2 cơ chế : DNS hoặc biến môi trường. Service có thể được cân bằng tải bởi Kubernetes. Tuy nhiên, dev có thể chọn tự quản lý việc loadbalance trong những trường hợp dùng resources bên ngoài hoặc các yêu cầu loadbalance đặc biệt mà Kube không cung cấp. 
## Volume 
Thời gian lưu trữ đi cùng với thời gian sống của pod. Tuy nhiên đôi khi cũng cần lưu lại data khi pod chết, hoặc sync data giữa các node với nhau.Nói chung Kube có support khúc này luôn ([rkt] cái này nè)(https://coreos.com/rkt/docs/latest/using-rkt-with-kubernetes.html). Có nhiều kiểu volume trên cloud  : network file systems, git repo.. Và phần vui nhất là [[https://kubernetes.io/docs/concepts/storage/persistent-volumes/](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)]
## Statfulset
Nếu quan tâm tới tính toàn vẹn của data. Đôi khi cần Kube quản lý việc distributed data như MySQL Galera.
## Secret
Chưa các thông tin nhạy cảm như access token. Lưu dưới dạng text trong [etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/). Được truy cập thông qua API. Chứ các thông tin để truy cập vào pod. Mục đích khác khi dùng secret đó là coi như biến môi trường :smile:. Và luôn được lưu trong memory. 
## Name 
Mỗi object trong kube được xác định duy nhất bởi UID. Thường được refer khi call API. 253 character là maximum :heart:
## Namespace :
Là một virtual cluster. Mỗi virtual cluster chỉ giao tiếp với nhau thông qua một public interfaces. Node objects và persistent volume không nằm trong namespace. Kube có thể lập lịch cho pods với nhiều namespace khác nhau trong cùng một node. Cũng như vậy, 	 pods từ namespace khác nhau có thể cùng một persistent storage

Khi dùng namespaces,  là bạn đã hiểu về network policy và resources để đảm bảo và quản lý tài nguyên của physical cluster
# Diving in Kube architecture in depth
## Distributed Design Systems patterns

### Sidecar pattern
Giả sử một container chỉ chịu trách nhiệm logging service nơi sẽ để lưu và xử lý log của cả hệ thống. Khi cần chỉ cần update logging service và deploy lên lại. Các applications sẽ không bị thay đổi và sẽ không bị terminated một loạt service :imp:. Đọc thêm về pattern này [sidecar pattern](https://dzone.com/articles/sidecar-design-pattern-in-your-microservices-ecosy-1)
## Ambassador pattern.

[https://www.magalix.com/blog/kubernetes-patterns-the-ambassador-pattern](https://www.magalix.com/blog/kubernetes-patterns-the-ambassador-pattern)

## Adaptor pattern
[https://www.magalix.com/blog/the-adapter-pattern](https://www.magalix.com/blog/the-adapter-pattern)

# Monitoring, Logging, and Trouble Shooting
## Node problem detector 
Là một pod chạy trên mỗi node. Phát hiện các hành vi khác nhau thông qua nhiều môi trường khác nhau, khác nhau phần cứng, khác nhau OS luôn :imp:.
## DaemonSet 
Là một pod trên mỗi pod. Một khi định nghĩa DaemonSet, mỗi node được add vào cluster tự đông. Kube sẽ start một instance tương tư của pod đó trên node đó. **Node Problem Detector (NPD)** được hiểu như là DaemonSet,
## Quotas, shares, and limits :
Ta có thể gặp những vấn đề như :
- Thiếu nguồn lực : nếu một pod cần nhiều hơn một node đang available thì pod không đc chạy :cry:
- Sử dụng dưới mức : dùng ít hơn nhiều so với khai báo. Lãng phí (Thất thoát kinh phí nhà nước)
- Khai báo sai : Just the same way :smile:
> Túm váy lại là nên kiểm tra trên dashboard để xem pod có đang dùng lãng phí cái nào không rồi config lại. That's it. Every one know what is waste :smile:

# High Availability and Reliability
## Creating highly available clusters
```etcd``` phải được deployed như một cluster (thường là 3 - 5 nodes, tại sao lại là 3 và 5 thì google :smile:). . Hiểu nôm na thì deployed càng nhiều node thì xác suất available của service càng tăng lên :smile: _kind of makesense, right?_

![](https://i.imgur.com/JdFseST.png)
## Live cluster upgrades
### Rolling upgrades
- Cluster sẽ chạy cả 2 phiên bản mới và cũ tại cùng một thời điểm. Tuy nhiên cần sẽ quan tâm tới trường hợp : thành phần mới tương thích với thành phần cũ và ngược lại.
- Với trường hợp thành phần mới tương thích với thành phần cũ, upgrade sẽ rất dễ. 
- Từ phiên bản 1.2 việc deployment resource sẽ dễ dàng hơn. 
### Complexity Deployment
Giả sử service A phụ thuộc vào service B. Giờ service B cần thay đổi. v1 pods service A không thể giao tiếp được với v2 pods service B. Nên ta cần implement v1 API cho service B. Tuy nhiên sẽ phức tạp hơn khúc deployment và yêu cầu nhiều bước. 
### Blue-green upgrades.
Chuẩn bị một bản copy hoàn thiện trên production env. Bây giờ có 2 bản. Hiện tại giả sử, blue(bản cũ) đang hoạt động và service các requests. Và có thể test trên bản còn lại. Một khi bản green(bản mới) okelah rồi. thì chuyển từ blue(cũ) sang green(mới). Và roll back cũng cực kì easy. Các vấn đề về lưu trữ và in memory sẽ không được giải quyết. Chỉ các thành phần độc lập và được chia sẽ chung trên lớp persistence

![](https://i.imgur.com/38OSJAO.png)

### Managing data contract changes
Data contracts diễn tả cách data được tổ chức. 

### Zero-downtime
Để hi vọng hệ thống của mình là một hệ thống zero-downtime :smile:
- Dự phòng ở mọi cấp độ. Không có điểm nào down làm cho toàn bộ system down.
- Tự động hot swapping cả thành phần lỗi. 
# Understander Kube Security
## Node challenges
- Kubelet là nơi để talk với API server. Nếu replace Kubelet bởi một bản khác, thì có thể truy cập vào vùng dùng chung.
- Resource drain.
- Các kiểu có thể bị tấn công :
	- Chiếm quyền kiểm soát host.
	- Replace kubelet
	- Run master components (API server, scheduler, controller manager)
	- Drains resources
## Network Challenges :
- Connect được thiết lập ra sao, planning như thế nào.
- Chọn các thành phần, giao thức, ports.
- Dynamic discovery service
- Public or private access
- Authentication and authorization
- Firewalls rules
- Network policy
- Key management and exchange
## Image challenges 
- Kube không biết images đang làm cái gì.
- Kube phải cung cấp cách thức truy cập resources
- Bảo vệ images 
- Tốc độ development và deployment
- Image chứa OS hết hạn
## Pod and Container challenge :
- Cùng một pod, container chia sẻ localhost network.
- Chia sẻ volume được mount, trên file host system.
## Understanding service accounts in Kube
More info : [https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/)
## Manageing network policies
### Choosing a supported networking solution 
Các kiểu support network policies của Kube :
- Calico
- 
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjIwMDA5NDg3LDc2Njk0OTg5MCwtMTk4Mj
M3MTEwLDQyNjI2NTM5Niw0MDc5ODkyMTgsMTg5NDEzODM4MSwx
ODExNzc0MDg3LC0xOTI2OTk2ODgyXX0=
-->