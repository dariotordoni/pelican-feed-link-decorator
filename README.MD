# Pelican feed link decorator
This plugin gets the feeds after their generation and just before they are written. Then adds utm parameters to all the links inside the feed and return it.

UTM parameters are customizable parameters added to a url that allow analytics softwares like Google Analytics to recognize the source and the medium of a visit, by the values assigned to utm_source and utm_medium.\
The value passed to utm_campaign, instead, helps to assign the visits to a specific marketing campaign.

Peopole visiting your website using a feed rss/atom aggregator, would be seen as coming from direct traffic without adding utms to the urls. Using this plugin you can change this behaviour and gets more insight from the vists of your website, to better understand which marketing channel works better for you.

The are several analytics softwares out there, Google Analytics is the most popular, so its parameters get often recognized also by the others.
At the time of writing, if you want to change these parameters you can do it manually editing the code of the plugin. I am planning to have settings variables inside the pelicanconf file, to manage them easier.
