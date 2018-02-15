import os


APItoken = os.getenv('IBMQE_API')

config = {
  'url': 'https://quantumexperience.ng.bluemix.net/api',
  'hub': None,
  'group': None,
  'project': None
}

if APItoken is None:
  raise Exception('Please set up your access token. See Qconfig.py.')
