"""Functions used by the macros mkdocs plugin."""
from . import schema, utils


def make_filename_template(**kwargs):
    """Generate a filename template snippet from the schema, based on specific
    filters.

    Parameters
    ----------
    kwargs : dict
        Keyword arguments used to filter the schema.
        Example kwargs that may be used include: "suffixes", "datatypes",
        "extensions".

    Returns
    -------
    codeblock : str
        A multiline string containing the filename templates for file types
        in the schema, after filtering.
    """
    schemapath = utils.get_schema_path()
    schema_obj = schema.load_schema(schemapath)
    codeblock = schema.make_filename_template(schema_obj, **kwargs)
    return codeblock


def make_filetree_example(filetree_info):
    """Generate a filetree snippet from example content.

    Parameters
    ----------
    filetree_info : dict

    Returns
    -------
    codeblock : str
        A multiline string containing the filetree example.
    """
    codeblock = schema.make_filetree_example(filetree_info)
    return codeblock


def make_entity_table(**kwargs):
    """Generate an entity table from the schema, based on specific filters.

    Parameters
    ----------
    kwargs : dict
        Keyword arguments used to filter the schema.
        Example kwargs that may be used include: "suffixes", "datatypes",
        "extensions".

    Returns
    -------
    table : str
        A Markdown-format table containing the corresponding entity table for
        a subset of the schema.
    """
    schemapath = utils.get_schema_path()
    schema_obj = schema.load_schema(schemapath)
    table = schema.make_entity_table(schema_obj, **kwargs)
    return table


def make_entity_definitions():
    """Generate definitions and other relevant information for entities in the
    specification.

    Returns
    -------
    text : str
        A multiline string containing descriptions and some formatting
        information about the entities in the schema.
    """
    schemapath = utils.get_schema_path()
    schema_obj = schema.load_schema(schemapath)
    text = schema.make_entity_definitions(schema_obj)
    return text
