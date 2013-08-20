from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.supermodel import model

from plone.app.textfield import RichText
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder


from collective.nonprofitprogrammes import MessageFactory as _
from collective.nonprofitprogrammes.project import IProject
#from collective.nonprofitprogrammes.programme import IProgramme
from collective.nonprofitprogrammes.partner import IPartner


# Interface class; used to define content-type schema.

class _IProgramme(form.Schema, IImageScaleTraversable):
    """
    Based Programme Profile
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/programme.xml to define the content type
    # and add directives here as necessary.

    form.model("models/programme.xml")


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class IProgramme(_IProgramme,model.Schema):
    """
    Programme Profile
    """

    related_programmes = RelationList(
    title=u"Related Programmes",
    default=[],
    value_type=RelationChoice(title=_(u"Related Programmes"),
                              source=ObjPathSourceBinder(object_provides=_IProgramme.__identifier__)),
    required=False,
)
    related_projects = RelationList(
    title=u"Related Projects",
    default=[],
    value_type=RelationChoice(title=_(u"Related Projects"),
                              source=ObjPathSourceBinder(object_provides=IProject.__identifier__)),
    required=False,
)
    partners = RelationList(
    title=u"Partners",
    default=[],
    value_type=RelationChoice(title=_(u"Related Partners"),
                              source=ObjPathSourceBinder(object_provides=IPartner.__identifier__)),
    required=False,
)

class Programme(dexterity.Container):
    grok.implements(IProgramme)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# programme_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class ProgrammeView(grok.View):
    grok.context(IProgramme)
    grok.require('zope2.View')

    # grok.name('view')
