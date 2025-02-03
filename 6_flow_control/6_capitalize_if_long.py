def capitalize_if_long(s):
    if len(s) > 10:
        return s.upper()
    return s

print(capitalize_if_long("short"))
print(capitalize_if_long("this is long"))