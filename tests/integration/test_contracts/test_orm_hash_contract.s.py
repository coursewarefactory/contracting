h = Hash()

@export
def set_h(k: str, v: int):
    h.set(k, v)

@export
def get_h(k: str):
    return h.get(k)
