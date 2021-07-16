# Overview Gas Price API from https://bscgas.info/

## Dependencies :
1. Web3 python (Similar web3j java)
2. Sanic framework (HttpServer)
3. numpy and another package relate for calculate data.

## Standard 
```python
SAFELOW  =  35

STANDARD  =  60

FAST  =  90
```
> Which mean gas price greater than 35% gas price total 200 block before
## Class 

> Class `Timers` :  class to keep track of time relative to network block
```python
class  Timers():

"""

class to keep track of time relative to network block

"""

    def  __init__(self, start_block):

        self.start_block  =  start_block

        self.current_block  =  start_block

        self.process_block  =  start_block

  

    def  update_time(self, block):

        self.current_block  =  block

        self.process_block  =  self.process_block  +  1
```

> Class `CleanTx()`  : information of transaction had been mined.

```python
class  CleanTx():

"""transaction object / methods for pandas"""

    def  __init__(self, tx_obj):

        self.hash  =  tx_obj.hash

        self.block_mined  =  tx_obj.blockNumber

        self.gas_price  =  tx_obj['gasPrice']

        self.round_gp_10gwei()

     def  to_dataframe(self):

        data  = {self.hash: {'block_mined':self.block_mined, 'gas_price':self.gas_price, 'round_gp_10gwei':self.gp_10gwei}}

        return  pd.DataFrame.from_dict(data, orient='index')

  

    def  round_gp_10gwei(self):

"""Rounds the gas price to gwei"""

        gp  =  self.gas_price/1e8

        if  gp  >=  1  and  gp  <  10:

            gp  =  np.floor(gp)

        elif  gp  >=  10:

            gp  =  gp/10

            gp  =  np.floor(gp)

            gp  =  gp*10

        else:

            gp  =  0

           self.gp_10gwei  =  gp
```

> Class `CleanBlock` : information of Block

```python
class  CleanBlock():

"""block object/methods for pandas"""

    def  __init__(self, block_obj, timemined, mingasprice=None):

        self.block_number  =  block_obj.number

        self.time_mined  =  timemined

        self.blockhash  =  block_obj.hash

        self.mingasprice  =  mingasprice

    def  to_dataframe(self):

        data  = {0:{'block_number':self.block_number, 'blockhash':self.blockhash, 'time_mined':self.time_mined, 'mingasprice':self.mingasprice}}

        return  pd.DataFrame.from_dict(data, orient='index')
```

## Main function :
```python
def write_to_json(gpreccs, prediction_table)
```

> Main functionality is create response gas price

```python
def  process_block_transactions(block)
```
> Get transaction from block number
> Return block data frame and block object

```python
def  process_block_data(block_df, block_obj) -> DataFrame
```

```python
def  get_hpa(gasprice, hashpower) -> int
```

> gets the hash power accepting the gas price over last 200 blocks

```python
def  analyze_last200blocks(block, blockdata)
```

```python
def  make_predictTable(block, alltx, hashpower, avg_timemined)
```


## Main follow
Before we prepare 100 blocks data before current block. (`alltx`, `blockdata`)

1. Get `mined_block_num`
2. ```(mined_blockdf, block_obj) = process_block_transactions(mined_block_num)```
3. Fill `None` value with data `mined_blockdf` from step 2.
4. Process block data `blockdata = process_block_data(mined_blockdf, block_obj)`
5. Append to data frame `block_data`
6. Get hash power table from last 200 blocks. (call `analyze_last200blocks()`)
7. Make prediction (call `make_predictTable()`)
8. Get gas price `get_gasprice_recs`
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjAzOTg5MzQ0XX0=
-->