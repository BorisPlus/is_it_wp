from is_it_wp import core
from sites import sites
from multiprocessing import Pool
import json


def check(domain):
    return core.check(domain)


def write_to_file(result):
    with open('result.json', 'aw', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write('\n')


if __name__ == "__main__":
    with Pool(5) as pool:
        r = pool.map_async(check, sites, callback=write_to_file)
        r.wait()
