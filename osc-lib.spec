#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : osc-lib
Version  : 1.6.0
Release  : 12
URL      : https://pypi.debian.net/osc-lib/osc-lib-1.6.0.tar.gz
Source0  : https://pypi.debian.net/osc-lib/osc-lib-1.6.0.tar.gz
Summary  : OpenStackClient Library
Group    : Development/Tools
License  : Apache-2.0
Requires: osc-lib-python
Requires: Babel
Requires: cliff
Requires: keystoneauth1
Requires: os-client-config
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: simplejson
Requires: six
Requires: stevedore
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=======
osc-lib
=======
.. image:: https://img.shields.io/pypi/v/osc-lib.svg
:target: https://pypi.python.org/pypi/osc-lib/
:alt: Latest Version

%package python
Summary: python components for the osc-lib package.
Group: Default

%description python
python components for the osc-lib package.


%prep
%setup -q -n osc-lib-1.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494268284
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1494268284
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
