import random
import secrets


def weak_rng(num_bytes: int) -> bytes:
    """Return a fixed number of non-cryptographic random bytes.

    :param num_bytes: The number of bytes to return
    :return: ‘biased’ bytes
    """
    # To overcome the annoying CPython implementation issue where
    # the number indicating how many bytes to fetch (not the actual bytes)
    # does not fit within a C int32.
    # We must thus not to query more than INT32_MAX / 8 bytes at a time.
    # Implementation details are the bane of cryptographers!
    limit = 0x0FFFFFFF
    if num_bytes < limit:
        return random.randbytes(num_bytes)

    res = b""

    # num_bytes = q * limit + r
    q, r = divmod(num_bytes, limit)
    for _ in range(q):
        res += random.randbytes(limit)

    return res + random.randbytes(r)


if __name__ == "__main__":
    num_bytes = 2 ** 32
    cs_rand = secrets.token_bytes(num_bytes)
    weak_rand = weak_rng(num_bytes)

    cs_world = secrets.choice([True, False])

    with open("../../challenge.bin", "wb") as b:
        with open("../../other.bin", "wb") as o:
            with open("../../answer.txt", "w") as a:
                if cs_world:
                    b.write(cs_rand)
                    o.write(weak_rand)
                    a.write("Random world")
                else:
                    b.write(weak_rand)
                    o.write(cs_rand)
                    a.write("Weak PRNG world")
