from host import Host


def host_process_cli(config, auth, opt):
    if opt['--delimiter'] is None:
        delimiter = " "
    else:
        delimiter = opt['--delimiter']

    if opt['--format'] is None:
        o_format = "text"
    else:
        o_format = opt['--format']

    n = Host(
        hostname=config.host,
        auth=auth,
        o_format=o_format,
        delimiter=delimiter
    )

    if opt['list'] is True:
        n.list_hosts()
    elif opt['search'] is True:
        n.search(
            name=opt['<name>'],
            site=opt['<site>'],
        )
    elif opt['get'] is True:
        network = opt['<network>']
        n.get(network)
    elif opt['fixedaddresses'] is True:
        network = opt['<network>']
        n.fixedaddresses(network)
    elif opt['create'] is True:
        name = opt['<name>']
        ipv4addrs = opt['<ipv4addrs>']
        mac = opt['<mac>']

        n.create_host(
            name,
            ipv4addrs,
            mac,
            disable=disable,
            members=members,
        )
        if n.api_out.has_error:
            print "Unable to Create Host: %s" % network
            sys.exit(2)
        else:
            print "Host Created Successfully"
            n.get(network)
    if opt['delete'] is True:
        network = opt['<network>']
        if network is not None:
            ret = n.delete_network(
                network,
            )
            if ret is False:
                print "Unable to delete network"
