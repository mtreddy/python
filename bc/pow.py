## Implementas proof of work in bit coln

import hashlib
import time


mnonce = 2 ** 32

def proof_of_work(new_header, diff_bits):
    target = 2 ** (256 - diff_bits)
    for nonc in xrange(mnonce):
        hnew = hashlib.sha256((str(new_header)) + str(nonce)).hexdigest()
        if long(hnew, 16) < target:
            print("Success with nonce %d" % nonce)
            print("Hash is %s" % hnew)
            return (hnew, nonce)
    printf("Failed after %d (mnonce) tries" % nonce)

if __name__ == '__main__':
    nonce = 0
    hresult = ''
    for diff_bits in xrange(32):
        diff = 2 ** diff_bits
        print("")
        print("Difficulty: %1d (%d bits)" % (diff, diff_bits))
        print("Starting search...")
        start_time = time.time()
        new_block = 'Hello this is new block' + hresult
        (hresult, nonce) = proof_of_work(new_block, diff_bits)
        end_time = time.time()
        elapsed_time = end_time - start_time 
        print("Elapsed time: %.4f seconds" % elapsed_time)
        if elapsed_time > 0:
            hash_power = float(long(nonce)/elapsed_time)
            print("Hashing power: %ld hashes per second" % hash_power)


