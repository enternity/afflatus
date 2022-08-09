# Raft note
Consensus algorithm for practical system typically have the following properties :
- They ensure safety (never return incorrect result) under all non Byzantine condition, include network delay, packet loss, duplication, reordering.
- They are fully functional (available) as long as many majority of the servers are operational and can communicate with each server and with clients. Thus, a typical cluster of five servers can tolerate the failure of any 2 servers. Servers are assumed to fail by stopping, they may later recover from state on stable storage and rejoin cluster.
- They do not depend on timing to ensure consistency of the logs, faulty clock and extreme message delay, at worst, cause availability of problems.
- In common case, a command can complete as soon as a majority of the cluster has responded to a single round of RPC calls, a minority of slow servers need not impact overall system performance.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjI3MTg1MTMxXX0=
-->