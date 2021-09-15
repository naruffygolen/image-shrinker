# coding : utf-8

if __name__ == '__main__':
    import sys
    import includes.im_utils as im_utils
    import includes.common as common
    valid_args = ('-f', '-r', '-o', '-h', '-v')

    args = sys.argv[1:]
    opt = common.cmd_options_value(args)

    for op in opt.keys():
        if op not in valid_args:
            im_utils.display_help("parameters")
            exit(-1)
    if '-h' in opt.keys():
        im_utils.display_help()
        exit(0)
    verbose = None
    if '-v' in opt.keys():
        verbose = 'v'
    try:
        file = opt['-f']
    except KeyError:
        im_utils.display_help("parameters")
    else:
        if '-r' in opt.keys():
            try:
                factor = int(opt['-r'])
            except ValueError:
                print("wrong parameters")
                im_utils.display_help("parameters")
                exit(-1)
            else:
                if '-o' in opt.keys():
                    output_file = opt['-o']
                    im_utils.shrink_image(rimage_path=file, rfactor=factor, routput=output_file, rverbose=verbose)
                else:
                    im_utils.shrink_image(rimage_path=file, rfactor=factor, rverbose=verbose)
        elif '-o' in opt.keys():
            if '-r' in opt.keys():
                try:
                    factor = int(opt['-r'])
                except ValueError:
                    print("wrong parameters")
                    im_utils.display_help("parameters")
                    exit(-1)
                im_utils.shrink_image(rimage_path=file, rfactor=factor, routput=opt['-o'], rverbose=verbose)
            else:
                im_utils.shrink_image(rimage_path=file, routput=opt['-o'], rverbose=verbose)
        else:
            im_utils.shrink_image(rimage_path=file, rverbose=verbose)

else:
    print("this module must be imported")