# Makefile to build a repo of notebooks with JupyterBook and Sphinx configured
# in a way that can be deployed locally, via github actions, and for live
# testing on a JupyterHub that's running the URL Proxy service.

# regular HTML build on local computers, this is the same command called
# by github actions (though there, we call it directly to avoid assuming
# on this Makefile exists in all repos)

## html      : Build Jupyter Book (default target).
html:
	jupyter-book build .

# Use this target to build the site on a hosted hub - it requires special configuration
# of Sphinx's html_baseurl parameter.

## html-hub  : build site for viewing on a hosted JupyterHub.
html-hub: conf.py
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	@echo "Start the Python http server to access the build."
	@echo "To do so, open a new terminal, and paste the following line in it:"
	@echo 
	@echo cd "${PWD}/_build/html && python -m http.server"
	@echo 
	@echo "Then, visit this URL in a new tab of your browser:"
	@echo "https://jackeddy.2i2c.cloud/user-redirect/proxy/8000/index.html"

# In order to test the book build on a JupyterHub cloud instance, we need to 
# call directly Sphinx, to work around the fact that JupyterBook doesn't let us
# configure the html_baseurl parameter. For this, we auto-generate the necessary
# Sphinx conf.py file from JBook's configuration. 
# Note: This file should never be edited or committed to version control!

## conf.py   : create Sphinx configuration (automatically called as needed).
conf.py: _config.yml _toc.yml
	jupyter-book config sphinx .


## clean     : Remove auto-generated build directory and other files.
.PHONY: clean
clean:
	rm -rf _build/html/ conf.py

## help      : print summary of all targets.
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
