%define module	foolscap

Name:		python-foolscap
Summary:	Remote object-messaging for Python+Twisted
Version:	24.9.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://github.com/warner/foolscap
Source0:	%{URL}/archive/%{module}-%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(versioneer)

%description
is an RPC/RMI (Remote Procedure Call / Remote Method Invocation) protocol
for use with Twisted, derived/inspired by Twisted's built-in
"Perspective Broker" package.

If you have control of both ends of the wire, and are thus not constrained
to use some other protocol like HTTP/XMLRPC/CORBA/etc, you might consider
using Foolscap.

Fundamentally, Foolscap allows you to make a python object in one process
available to code in other processes, which means you can invoke its methods
remotely.

This includes a data serialization layer to convey the object graphs
for the arguments and the eventual response, and an object reference system to
keep track of which objects you are connecting to.

It uses a capability-based security model, such that once you create a
non-public object, it is only accessible to clients to whom you've given
the (unguessable) FURL.

You can of course publish world-visible objects that have well-known FURLs.


%files
%doc doc README.md
%license LICENSE
%{_bindir}/{flogtool,flappserver,flappclient}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}-py%{pyver}.egg-info
