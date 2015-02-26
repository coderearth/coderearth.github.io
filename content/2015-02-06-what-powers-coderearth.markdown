Title: "What Powers CoderEarth.org - Pelican and Github Pages"
Date: 2015-02-26 16:40
Category: Blog
Authors: Suhas
Tags: Architecture, Blog


My friend Kunal & I bought this domain on GoDaddy a year ago. Initially, I was planning to run this website on a shared host with the wordpress stack for content management. However this had its own cons, namely:

* Monthly rent for a shared host
* WordPress - is getting a little old
* Doesn't have the "hacker" feel to it

Mainly motivated by the third point above, I stumbled on [Octopress](http://octopress.org/) for content management and [Github Pages](https://pages.github.com/) for hosting - which seemed like a perfect fit for my needs.

Whenever I have a technology decision to make, I use the following tools to help me out:

* Github Stars - If the project isn't open source and not on Github, that's a huge let down for me - take a look at https://staticsitegenerators.net/
* [Google Trends](http://www.google.co.in/trends/) - To measure if the particular technology is trending
* StackOverflow - haven't we all been there, done that?

### Using Octopress 

I started using Octopress, and instantly liked it - everything had a fluid feeling to it, and I followed the below routine:

* Installed Ruby via `rvm` and [setup my environment](http://octopress.org/docs/setup/).
* Used `rake new_post['awesome_post_name']` to create a post and started editing the markdown file in my favorite text editor - `vim`.
* Deployed to Github Pages (after configuring the CNAME in GoDaddy) via just `rake deploy` - that's *after* setting up github pages with `rake setup_github_pages`

Everything was well and good - *until now*. Suddenly, Two things were blocking me from proceeding further: 

1. I come from a Python background -- at least 4 years of Python coding experience now, and I'm really comfortable with the entire Python ecosystem. I haven't yet been entirely comfortable with Ruby's gems and rakes.
2. I had a work dependency to move to a Windows-only laptop -- and Windows makes it a little harder to manage Octopress.

### Pelican to the rescue

[Pelican](http://blog.getpelican.com/) is a fantastic static site generator in the Python environment.

If you have Python and `pip` installed in your computer, getting pelican is as easy as `pip install pelican`. Once this is done, just give its [official docs](http://docs.getpelican.com/en/3.5.0/) a good read, and you're good to go. It has many cool features; here are a few:

* Blog posts in markdown
* `Python -m SimpleHTTPServer` for local viewing pleasure
* Easy github deployment using `ghp_import` (like, *really* easy)
* Theming support (this site is powered by a Bootstrap3 theme)

Here's the workflow that I currently follow:

1. Use Sublime Text 3 for writing markdown posts in the `SITE/content/` folder
2. Stay on the `source` branch, that's `git checkout -b source`
3. Run `pelican content` under `SITE/` which will generate the `SITE/output` folder
4. Run `ghp-import output` under `SITE/` which will create the `gh-pages` branch (Check using `git branch` if you feel so)
5. Run `git push -f origin gh-pages:master` which pushes the `gh-pages` branch on the master
6. Add all of the content and pelican files to the `source` branch and `git push origin source` - now the pelican raw files are on source and the blog html is on master and Github pages does its magic 

That's it. This entire blog is powered by Pelican and hosted on Github Pages. Why don't you give it a try too?