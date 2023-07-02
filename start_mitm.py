import asyncio
from mitmproxy import options
from mitmproxy.tools import dump
from mitmproxy.tools.main import mitmdump
from mitmproxy import ctx
import get_mitm_properties

mitm_host=get_mitm_properties.get_mitm_host()
mitm_port=int(get_mitm_properties.get_mitm_port())

class RequestLogger:
    def request(self, flow):
        url_request: str = str(flow.request.pretty_url)
        print('request is::::',flow.request)
        if flow.request.headers['shutdown']: #shut the proxy down if header shutdown is received
            print("Shutting down the proxy due to shutdown header")
            ctx.master.shutdown()
        
    def response(self,flow):
        url_request: str = str(flow.request.pretty_url)
        if 'text' in url_request:    #filter by request url   
            print('response is::::',flow.response.content.decode())

async def start_proxy(host, port):
    opts = options.Options(listen_host=host, listen_port=port)
    master = dump.DumpMaster(
        opts,
        with_termlog=False,
        with_dumper=False,
    )
    master.addons.add(RequestLogger())

    await master.run()
    return master

if __name__ == '__main__':
    asyncio.run(start_proxy(mitm_host, mitm_port))
