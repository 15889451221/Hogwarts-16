
def black_wrapper(fun):
    def run(*args,**kwargs):
        basepage = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e :
            for black in basepage.black_list:
                eles = basepage.finds(*black)
                if len(eles)>0:
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e

    return run