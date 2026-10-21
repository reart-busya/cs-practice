paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

def count_by_extension(paths):
    ext_counts = {}
    for p in paths:
        ext = p.split(".")[-1].lower() if "." in p else ""
        ext_counts[ext] = ext_counts.get(ext, 0) + 1
    return ext_counts

def deepest_path(paths):
    best = ""
    max_ext_count = -1
    for p in paths:
        ext_count = p.count("/")
        if ext_count > max_ext_count or (ext_count == max_ext_count and p < best):
            best = p
            max_ext_count = ext_count
    return best

def human_size(n_bytes):
    size = n_bytes
    if size < 1024:
        return str(size) + " Б"
    else:
        i = 0
        while size >= 1024:
            size /= 1024
            i += 1
        if i == 1:
            return ("%3.1f %s" % (size, "КБ"))
        if i == 2:
            return ("%3.1f %s" % (size, "МБ"))
        if i == 3:
            return ("%3.1f %s" % (size, "ГБ"))
        if i == 4:
            return ("%3.1f %s" % (size, " ТБ"))

print(count_by_extension(paths))
print(deepest_path(paths))
print(human_size(900))
print(human_size(1536))
print(human_size(5 * 1024 * 1024))