# Components of a blockchain.
-   A peer-to-peer (P2P) network connecting participants and propagating transactions and blocks of verified transactions, based on a standardized "gossip"  protocol
    
-   Messages, in the form of transactions, representing state transitions
    
-   A set of consensus rules, governing what constitutes a transaction and what makes for a valid state transition
    
-   A state machine that processes transactions according to the consensus rules
    
-   A chain of cryptographically secured blocks that acts as a journal of all the verified and accepted state transitions
    
-   A consensus algorithm that decentralizes control over the blockchain, by forcing participants to cooperate in the enforcement of the consensus rules
    
-   A game-theoretically sound incentivization scheme (e.g., proof-of-work costs plus block rewards) to economically secure the state machine in an open  environment
    
-   One or more open source software implementations of the above ("clients")

# Ethereum's Components :
P2P network

Ethereum runs on the  _Ethereum main network_, which is addressable on TCP port 30303, and runs a protocol called  _ÐΞVp2p_.

Consensus rules

Ethereum’s consensus rules are defined in the reference specification, the Yellow Paper (see  [Further Reading](https://github.com/ethereumbook/ethereumbook/blob/develop/01what-is.asciidoc#references)).

Transactions

Ethereum transactions are network messages that include (among other things) a sender, recipient, value, and data payload.

State machine

Ethereum state transitions are processed by the  _Ethereum Virtual Machine_  (EVM), a stack-based virtual machine that executes  _bytecode_  (machine-language instructions). EVM programs, called "smart contracts," are written in high-level languages (e.g., Solidity) and compiled to bytecode for execution on the EVM.

Data structures

Ethereum’s state is stored locally on each node as a  _database_  (usually Google’s LevelDB), which contains the transactions and system state in a serialized hashed data structure called a  _Merkle Patricia Tree_.

Consensus algorithm

Ethereum uses Bitcoin’s consensus model, Nakamoto Consensus, which uses sequential single-signature blocks, weighted in importance by PoW to determine the longest chain and therefore the current state. However, there are plans to move to a PoS weighted voting system, codenamed  _Casper_, in the near future.

Economic security

Ethereum currently uses a PoW algorithm called  _Ethash_, but this will eventually be dropped with the move to PoS at some point in the future.

Clients

Ethereum has several interoperable implementations of the client software, the most prominent of which are  _Go-Ethereum_  (_Geth_) and  _Parity_.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg3NzI2MDg5Nl19
-->