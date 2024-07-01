from nacl.signing import VerifyKey
from config import public_key


async def verify_key(
    raw_body: bytes, signature: str, timestamp: str, client_public_key: str
) -> bool:
    message = timestamp.encode() + raw_body
    try:
        vk = VerifyKey(bytes.fromhex(client_public_key))
        vk.verify(message, bytes.fromhex(signature))
        return True
    except Exception as ex:
        print(ex)
    return False


async def verify_request_signature(request) -> bool:
    signature = request.headers.get("X-Signature-Ed25519")
    timestamp = request.headers.get("X-Signature-Timestamp")
    request_body = await request.read()

    if (
        not signature
        or not timestamp
        or not await verify_key(request_body, signature, timestamp, public_key)
    ):
        return False
    return True
