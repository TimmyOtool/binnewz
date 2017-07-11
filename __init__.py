from .main import binnewz
from couchpotato.core.logger import CPLog

log = CPLog(__name__)

def autoload():
    log.debug('load success')
    return binnewz()

config = [{
    'name': 'binnewz',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'nzb_providers',
            'name': 'binnewz',
            'description': 'Free provider, lots of french nzbs. See <a href="http://www.binnews.in/">binnewz</a>',
            'wizard': True,
            'icon': 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAgRJREFUOI1t009rVFcYx/HPuffOTGYmMcZoEmNUkiJRSZRAC1ropuimuy6KuHHhShe+EF+CL8AX4LpQCgoiohhMMKKMqHRTtaJJ5k8nudfFnBkjzoEf5zk8PN/zO3+egFGMYX+MS9hFG604d/A/ulG7yFFkqOGgcuUuSJK32q0NPMMaNrE9RC10UxzCedX6767cqDu2MGV8YlFz62ed9iWVkYvy/IyimEUSFaKD3QwV7ENwapmlHymVU5126tNHVh9MW3s8bfXhOW8b16TpliR5otW8jm6GHiSEYOYoF076Zjx6x29/8OHfssZzNp6Ou3XzF8zicxYtZWBislfUKL4CFgIvd5mcYuowed7PjKOSGTYWwiAsij6srChmJI058Q6qyIYD9jgIIQzWxXygPtZPpUj6gGJv/V4HGoViPsLWt77bK9P7FDtg8zPr21RrX48wT3g11OcA0MG2oii8aXB4jiInK5FmSAcOGBUawwFvtFuJO7dpbLBynuM/UK0Jn0YolXtqNfn4vl/bRZ7pfcsXdrqX3f/rhgd/L+m0J8zMdZ1eKTn7U7C4zNg+yhX+ed2/syZ2AkZQ12umSRyI8wpOqdaXdTszRmocOR5Mz2bu/ZnL81/xIsTnyFCOsKpeg9ViPBo1jxMq1UVpEjS3r+K/Pe81aJQ0qhShlQiuxPxOtL+J1heOZZ0e63LUQAAAAABJRU5ErkJggg==',
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 0,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]
