DJANGO JOB PORTAL
=================

A django skill focused job portal.

View a running instance at [http://djangojobportal](http://djangojobportalurl)


Note that whilst usable, Djangojobportal is under continual development and not
yet feature complete.

The latest source code is available at
[https://github.com/djangojobportal/djp](https://github.com/djangojobportal/djp).

* **Developers:** See our [developer guide](README-dev.md)
* **For production:** See our [deployment guide](README-docker.md)
* **For contribution:** See our [contribution guide](README-contrib.md)


Key features
------------

* Coming soon - Loading ...


Project Activity
----------------

Story queue on Waffle:

* [![Stories in Ready](https://badge.waffle.io/djangojobportal/djp.svg?label=ready&title=Ready)](http://waffle.io/djangojobportal/djp) 
* [![Stories in In Progress](https://badge.waffle.io/djangojobportal/djp.svg?label=in%20progress&title=In%20Progress)](http://waffle.io/djangojobportal/djp)

[![Throughput Graph](https://graphs.waffle.io/djangojobportal/djp/throughput.svg)](https://waffle.io/djangojobportal/djp/metrics)

* Current test status master: [![Build Status](https://travis-ci.org/djangojobportal/djp.svg?branch=master)](https://travis-ci.org/djangojobportal/djp) and [![Code Health](https://landscape.io/github/djangojobportal/djp/master/landscape.svg?style=flat)](https://landscape.io/github/djangojobportal/djp/master)

* Current test status develop: [![Build Status](https://travis-ci.org/djangojobportal/djp.svg?branch=develop)](https://travis-ci.org/djangojobportal/djp) and
[![Code Health](https://landscape.io/github/djangojobportal/djp/develop/landscape.svg?style=flat)](https://landscape.io/github/djangojobportal/djp/develop)

* Test coverage [![codecov](https://codecov.io/gh/djangojobportal/djp/branch/develop/graph/badge.svg)](https://codecov.io/gh/djangojobportal/djp)

Quick Installation Guide
------------------------

For deployment we use [docker](http://docker.com) so you need to have docker
running on the host. Djp is a django app so it will help if you have
some knowledge of running a django site.

```
git clone git://github.com/djangojobportal/djp.git
cd djp/deployment
cp btsync-db.env.EXAMPLE btsync-db.env
cp btsync-media.env.EXAMPLE btsync-media.env
make build
make permissions
make web
# Wait a few seconds for the DB to start before to do the next command
make migrate
make collectstatic
make devweb
```

If you need backups, put btsync keys in these files. If you don't need backups,
you can let the default content.

So as to create your admin account:
```
make superuser
```

**google authentication**

In social auth to use the google authentication you need to go to:

https://console.developers.google.com/apis/credentials

Create and oath2 credential with these options:

Authorized redirect URIs

http://<your domain>/en/complete/google-oauth2/

Use the Djangojobportal admin panel to set up the google account with your id and
secret


**Backups**

If you wish to sync backups, you need to establish a read / write btsync
key on your production server and run one or more btsync clients
with a read only key.

```
cd deployment
cp btsync-media.env.EXAMPLE btsync-media.env
cp btsync-db.env.EXAMPLE btsync-db.env
```

Now edit the ``btsync-media.env`` and ``btsync-db.env`` files, including
relevant SECRET and DEVICE settings.

Participation
-------------

We work under the philosophy that stakeholders should have access to the
development and source code, and be able to participate in every level of the
project - we invite comments, suggestions and contributions.  See
[our milestones list](https://github.com/djangojobportal/djp/milestones) and
[our open issues list](https://github.com/djangojobportal/djp/issues?page=1&state=open)
for known bugs and outstanding tasks. You can also chat live with our developers
and community members using the link below.

Chart [web.flock.com/](https://web.flock.com/)

Credits
-------

Djp was developed by [djangojobportal.com](http://djangojobportal.com) and
individual contributors.

License
------

Djp is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License version 3 (GPLv3) as
published by the Free Software Foundation.

The full GNU General Public License is available in LICENSE.txt or
http://www.gnu.org/licenses/gpl.html


Disclaimer of Warranty (GPLv3)
------------------------------

There is no warranty for the program, to the extent permitted by
applicable law. Except when otherwise stated in writing the copyright
holders and/or other parties provide the program "as is" without warranty
of any kind, either expressed or implied, including, but not limited to,
the implied warranties of merchantability and fitness for a particular
purpose. The entire risk as to the quality and performance of the program
is with you. Should the program prove defective, you assume the cost of
all necessary servicing, repair or correction.

Thank you
---------

[![PyCharm](https://cloud.githubusercontent.com/assets/1421861/16826865/4cde910c-49ab-11e6-95ae-48cf21f3a69f.png)](https://www.jetbrains.com/pycharm) 

We use [PyCharm](https://www.jetbrains.com/pycharm) for our python development work.

Thank you to the individual contributors who have helped to build Djangojobportal:

* Alison Mukoma: mukomalison@gmail.com
* Mario Osorio: nimbiotics@gmail.com
* Loading list ...
