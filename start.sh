aria2c --enable-rpc --rpc-listen-all=false --rpc-allow-origin-all --daemon --max-tries=50 --retry-wait=3 --continue=true && python3 terabox.py && python3 ok.py
