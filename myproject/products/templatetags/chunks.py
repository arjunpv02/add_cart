from django import template

register=template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    if not list_data:
        return []  # Return an empty list if list_data is None or empty
    chunk_size = int(chunk_size)
    chunk = []
    for i, data in enumerate(list_data):
        chunk.append(data)
        if (i + 1) % chunk_size == 0:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


    
    
"""Filter Registration:
register = template.Library() initializes the template library for custom filters.
@register.filter(name='chunks') registers the chunks function as a template filter named chunks.
Chunks Function:
The function takes a list (list_data) and a chunk size (chunk_size).
It checks if list_data is empty or None and returns an empty list if true.
It converts chunk_size to an integer.
It iterates over list_data, appending items to a temporary list (chunk).
When the chunk size is reached, it yields the chunk and resets the temporary list.
After the loop, if there are remaining items in the temporary list, it yields the final chunk."""

