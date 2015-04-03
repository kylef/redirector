import fnmatch
from yaml import load
from rivr.views import RedirectView
from rivr.wsgi import WSGIHandler


class Redirector(RedirectView):
    def get_redirect_url(self, **kwargs):
        host = self.request.host.split(':')[0]
        print host

        for redirect in self.redirects:
            if fnmatch.fnmatch(host, redirect['host']):
                parameters = {
                    'scheme': self.request.scheme,
                    'host': host,
                    'zones': host.split('.'),
                    'path': self.request.path
                }

                return redirect['destination'].format(**parameters)


with open('redirector.yaml') as fp:
    config = load(fp)


view = Redirector.as_view(permanent=False, redirects=config)
wsgi = WSGIHandler(view)


if __name__ == '__main__':
    from rivr.server import serve
    serve(view)

