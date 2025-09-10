import json
import hashlib


def compute_hash(json_data):
    """
    Computes a SHA-256 hash of a given JSON object.

    Args:
        json_data (dict or list): The JSON object to hash.

    Returns:
        str: The hexadecimal representation of the SHA-256 hash.
    """
    # 1. Serialize the JSON object into a canonical string.
    #    - sort_keys=True ensures consistent key order.
    #    - separators=(',', ':') removes unnecessary whitespace.
    #    - ensure_ascii=False handles non-ASCII characters correctly.
    json_string = json.dumps(json_data, sort_keys=True, separators=(',', ':'), ensure_ascii=False)

    # 2. Encode the string to bytes (UTF-8 is a common choice).
    json_bytes = json_string.encode('utf-8')

    # 3. Compute the SHA-256 hash.
    sha256_hash = hashlib.sha256(json_bytes).hexdigest()

    return sha256_hash
