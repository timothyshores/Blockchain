import hashlib
from time import time
from uuid import uuid4

# Paste your version of blockchain.py from the basic_block_gp
# folder here

# Instantiate Node
app = Flask(_name_)
# Generate a globally unqiue address for this node
node_identifier = str(uuid4()).replace('-', '')
# Instantiate Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['POST'])
def mine():
    #Determine if proof is valid
    last_block = blockchain.last_block
    last_block_string = json.dumps(last_block, sort_keys=True)

@property
def last_block(self):
    return self

@app.route('/last_block', method=['GET'])
def last_block():
    response = {
        'last_block': blockchain.last_block
    }
    return jsonify(response), 200

if __name__ == '__main__':
    if len(sys.args)