import time
from backend.blockchain.blockchain import Blockchain

blockchain = Blockchain()

times = []

for i in range(1000):
    start_time = int(time.time())
    blockchain.add_block(i)
    end_time = int(time.time())

    time_to_mine = end_time - start_time
    times.append(time_to_mine)

    average_time = sum(times) / len(times)

    print(f'New block difficulty: {blockchain.chain[-1].difficulty}')
    print(f'Time to mine new block: {time_to_mine}s')
    print(f'Average time to add blocks: {average_time}s\n')
