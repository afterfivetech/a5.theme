from collective.grok import gs
from a5.theme import MessageFactory as _

@gs.importstep(
    name=u'a5.theme', 
    title=_('a5.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('a5.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
