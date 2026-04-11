#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Modulun içindəki bütün adları alırıq
    all_names = dir(hidden_4)

    # Əlifba sırası ilə düzürük və __ ilə başlamayanları çap edirik
    for name in sorted(all_names):
        if not name.startswith("__"):
            print("{}".format(name))
