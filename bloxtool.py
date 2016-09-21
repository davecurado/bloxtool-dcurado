#!/usr/bin/python
"""bloxtool.py

Usage:
  bloxtool.py fixedaddress search mac <mac_address> [--config=~/.bloxtool.cfg][--delimiter=" "][--format=text]
  bloxtool.py fixedaddress search address <ipv4addr> [--config=~/.bloxtool.cfg][--delimiter=" "][--format=text]
  bloxtool.py fixedaddress create <name> <ipv4addr> <mac_address> [--config=~/.bloxtool.cfg][--delimiter=" "][--format=text]
  bloxtool.py fixedaddress delete mac <mac_address> [--config=~/.bloxtool.cfg][--delimiter=" "][--format=text]
  bloxtool.py fixedaddress delete address <ipv4addr> [--config=~/.bloxtool.cfg][--delimiter=" "][--format=text]
  bloxtool.py fixedaddress option <option> value <value> address <ipv4addr>[--config=~/.bloxtool.cfg][--delimiter=" "][--format=text][--delete]
  bloxtool.py network list [--config=~/.bloxtool.cfg][--delimiter=" "][--format=text][--extattrs]
  bloxtool.py network fixedaddresses <network> [--config=~/.bloxtool.cfg][--delimiter=" "][--format=text]
  bloxtool.py network get <network> [--config=~/.bloxtool.cfg][--delimiter=" "][--format=text]
  bloxtool.py network delete <network> [--config=~/.bloxtool.cfg][--delimiter=" "][--format=text]
  bloxtool.py network search name <name> [--delimiter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool.py network search site <site> [--delimiter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool.py network search attribute <attribute> value <value>[--network=""][--delimiter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool.py network create name <name> network <network> [--members=[]][--comment=" "][--disable=True][--config=~/.bloxtool.cfg]
  bloxtool.py network create range name <name> start <start> end <end>[--comment=" "][--disable=True][--config=~/.bloxtool.cfg]
  bloxtool.py network option create <option> value <value> network_block <network_block>[--config=~/.bloxtool.cfg][--delimiter=" "][--format=text][--delete]
  bloxtool.py network attr create <option> value <value> network_block <network_block>[--config=~/.bloxtool.cfg][--delimiter=" "][--format=text][--delete]
  bloxtool.py networkcontainer create name <name> network <network> [--members=[]][--comment=" "][--disable=True][--config=~/.bloxtool.cfg]
  bloxtool.py networkcontainer delete <network> [--config=~/.bloxtool.cfg][--delimiter=" "][--format=text]
  bloxtool.py networkcontainer option create <option> value <value> network_block <network_block>[--config=~/.bloxtool.cfg][--delimiter=" "][--format=text][--delete]
  bloxtool.py host search mac <mac_address>[--delimiter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool.py host create mac <mac_address> ipv4addrs=<ipv4addrs> name=<name>[--delimiter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool.py host list [--delimiter=" "][--format=text][--config=~/.bloxtool.cfg]

  bloxtool.py member list [--config=~/.bloxtool.cfg]

Options:
  -h --help     Show this screen.
  members is a comma separated list of members
"""  # nopep8
from docopt import docopt
from config import get_config
from fixedaddress_process_cli import fixedaddress_process_cli
from network_process_cli import network_process_cli
from networkcontainer_process_cli import networkcontainer_process_cli
# from host_process_cli import host_process_cli
import os


if __name__ == '__main__':
    opt = docopt(__doc__, version='bloxtool version 0.1.0')
    if opt['--config']:
        config_path = opt['--config']
    else:
        config_path = os.path.join(os.environ["HOME"], ".bloxtool.cfg")
    config = get_config(config_path)
    auth = (config.username, config.password,)
    if opt['fixedaddress']:
        fixedaddress_process_cli(config, auth, opt)
    elif opt['network'] and not opt['networkcontainer']:
        network_process_cli(config, auth, opt)
    elif opt['networkcontainer']:
        print 'here'
        networkcontainer_process_cli(config, auth, opt)
#    elif opt['host']:
#        host_process_cli(config, auth, opt)
