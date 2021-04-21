def add_cors(get_response):
    def addHeader(req):
        res=get_response(req)
        res.__setitem__('Access-Control-Allow-Origin', '*')
        return res
    return addHeader
    
