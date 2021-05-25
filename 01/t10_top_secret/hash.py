import hashlib

def md5_hash(str):
    print(f"""Original string: {str}
md5 hash generated is
{hashlib.md5(str.encode()).hexdigest()}""")


def sha1_hash(str):
    print(f"""Original string: {str}
sha1 hash generated is
{hashlib.sha1(str.encode()).hexdigest()}""")
