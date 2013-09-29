from zope import schema
from plone.directives import dexterity, form
from plone.namedfile.interfaces import IImageScaleTraversable

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