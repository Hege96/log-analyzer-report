def status_counts(entries):
    print(entries)
    status_counts= {}
    for i in entries:
        if "status" not in i:
            continue
        code=i["status"]
        status_counts[code]=status_counts.get(code,0)+1
    return sorted(status_counts.items(), key=lambda x: x[1], reverse=True)

def top_ips(entries):
    ips_counts={}
    for i in entries:
        if "ip" not in i:
            continue
        ip=i["ip"]
        ips_counts[ip]=ips_counts.get(ip, 0)+1
    return sorted(ips_counts.items(), key=lambda x:x[1], reverse=True)

def top_paths(entries):
    paths_count={}
    for i in entries:
        if "path" not in i:
            continue
        path=i["path"]
        paths_count[path]=paths_count.get(path, 0)+1
    return sorted(paths_count.items(), key=lambda x:x[1], reverse=True)

