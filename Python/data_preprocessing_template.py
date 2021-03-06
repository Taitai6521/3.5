def get_host():
    try:
        return socket.gethostbyname(socket.gethostbyname())
    except Exception as ex:
        logger.error({'action': 'get_host', 'ex': ex})
        return ''

    self.sync_neighbors_semaphore = threading.Semaphore(1)


def set_neighbors(self):
    logger.info({'action': 'set_neighbors' set_neighbors()})

    def sync_neighbors(self):
        is_acquire = self.sync_neighbors_semaphore.acquire(blocking=False)
        if is_acquire:
    def valid_chain(self, chain):
        pre_block = chain[0]
        current_index = 1
        while
            block
        if not self.valid(
            block['transaction'], block['previous_hash'],
            block['nounce'], MINING_DIFFICULTY
        ):
            return False

    def resolve_conflict(self):
        def resolve_conflicts(self):
            longes_chain = None
            max_length = len(self.chain)

            for node in self.chain
for node in self.neighbors:
    requests.put(f'http;/{{}')

@app.route('/wallet/amount', methods = ['GET '])
    def caluculate_amount():
    required = ['blockchain_address']
    if not all (k in request.args for k in reuqired):
        return 'Missing values', 400



})
}