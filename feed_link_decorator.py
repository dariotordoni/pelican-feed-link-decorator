from pelican import signals

FUD_DEFAULT = {
    'parameters': '?utm_campaign=rss&utm_source=blog&utm_medium=rss'
}

def feed_link_decorator(context, feed):
    """It gets the feeds after their generation and just before they are written. Then add utm parameters to all the links inside the feed"""
    for item in feed.items:
        current_link = item['link']
        # print(current_link)
        new_link = current_link + FUD_DEFAULT['parameters']
        item['link'] = new_link
        # print(item)
    return feed


def register():
    signals.feed_generated.connect(feed_link_decorator)