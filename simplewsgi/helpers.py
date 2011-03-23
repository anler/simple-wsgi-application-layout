# -*- coding: utf-8 -*-

import re, string
import unidecode

def remove_weird_characters(text):
    """
    Removes accents and other strange characters from a text
    """
    return unidecode.unidecode(text)

def to_slug(string, separator="-"):
    """
    Substitute string spaces by 'separator's
    Also delete '%' and '/' characters
    """
    string = ' '.join(string.split('-'))
    return re.sub('[\%/]', '', separator.join(string.lower().split()))

def from_slug(string, separator="-"):
    """Substitute string 'separator's by spaces"""
    return " ".join(string.split(separator))

def to_unicode(obj, encoding="utf-8"):
    """Converts obj to unicode if proceed"""
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = obj.decode(encoding)
    return obj

def excerpt(text, words, excerpt_string="...", limit=300, min_fragment_length=20):
    """
    Returns text limited to limit trying to include many words matches as 
    possible.
    To do so, text is fragmented dividing it in bunches by means of 
    excerpt_string. Every bunch of text has to be longer than min_fragment_length.
    """
    import re
    text = to_unicode(text)
    non_alphanum = re.compile("[^\w\d]", re.UNICODE)
    words = [re.escape(non_alphanum.sub("", to_unicode(word))) for word in words if word]
    #if len(word) < 3, word is not cosidered to make groups
    words = filter(lambda w: len(w) > 2, words)

    if len(words) == 0 or len(text) < limit:
        if len(text) > limit:
            text = text[:limit]
        return text

    else:

        def fragment_len(groups_len):
            return max(min_fragment_length, limit / (2 * groups_len))

        pattern = re.compile("((?i)%s)" % "|".join(words), re.UNICODE)
        groups = []
        for match in pattern.finditer(text):
            start, end = match.start(), match.end()
            groups.append((start, end))
       
        # If there is not matches and len(text) > limit
        if len(groups) == 0:
            return text[:limit/2] + text[-limit/2:]

        index = 0

        while groups:
            try:
                balength = fragment_len(len(groups))
                first  = groups[index]
                second = groups[index + 1]

                if second[0] - balength > first[1]:
                    index += 1
                    continue
                else:
                    first = groups.pop(index)
                    groups[index] = (first[0], second[1])
            except IndexError:
                break

        excerpt = ""
        balength = fragment_len(len(groups))
        for group in groups:
            if group[0] - balength >= 0:
                excerpt += excerpt_string + text[group[0] - balength:group[1]]
            else:
                excerpt += text[0:group[1]]
            excerpt += text[group[1]:group[1] + balength]

        if len(groups) == 1:
            if len(excerpt) < limit:
                excerpt += excerpt_string + text[groups[0][1] + balength:limit]
            else:
                excerpt = excerpt[0:limit]
        if excerpt == "":
            excerpt = text[0:limit]
        excerpt += excerpt_string

        return excerpt[:limit-len(excerpt_string)] + excerpt_string


