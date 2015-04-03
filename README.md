# redirector

Simple web server for HTTP redirecting from one domain to another.

## Usage

### Configuration

Configuration is stored in `redirector.yaml` as a YAML file.

```yaml
- host: '*.fuller.li'
  destination: http://{zones[0]}.kylefuller.co.uk{path}
- host: '*querykit.org'
  destination: https://github.com/QueryKit
```

Where any sub-domain of fuller.li will redirect to the (sub-domain).kylefuller.co.uk/path

#### Example

| Request | Redirect |
|---------|----------|
| `http://mail.fuller.li/login` | `http://mail.kylefuller.co.uk/login` |
| `http://www.querykit.org/something` | `https://github.com/QueryKit` |

#### Supported Variables

- scheme
- host
- path
- zones (list) - A list of each domain component

### Deploying on Heroku

Click the button below to automatically set up the redirector on your own Heroku account.

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/kylef/redirector)

Once you've deployed, you can easily clone the application and alter the configuration to configure your own domains.

```bash
$ heroku clone -a new-app-name
$ cat redirector.yaml
```

Remember to configure your [custom domains](https://devcenter.heroku.com/articles/custom-domains) on Heroku:

```bash
heroku domains:add *.example.com
```

### Running the development server

```bash
$ pip install -r requirements.txt
$ python redirector.py
```

## License

redirector is released under the BSD license. See [LICENSE](LICENSE).
