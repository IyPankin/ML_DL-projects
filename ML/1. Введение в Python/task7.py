def find_modified_max_argmax(L, f):
    t = [f(k) for k in L if type(k) is int]
    if t:
        return (m := max(t), t.index(m))
    else:
        return ()
