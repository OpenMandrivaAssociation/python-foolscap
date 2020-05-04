%define module	foolscap

Summary:	Rewrite of Perspective Broker
Name:		python-%{module}
Version:	20.4.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://foolscap.lothar.com/
Source0:	https://files.pythonhosted.org/packages/65/de/fac1106cec1b49ff29f6aabb588b65377b81909b43794123f2ff2eea18f9/foolscap-20.4.0.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
Requires:	python >= 2.4
Requires:	python-twisted >= 2.5.0
Requires:	python-OpenSSL >= 0.6

%description
Foolscap is a ground-up rewrite of Perspective Broker, which itself is
Twisted's native RPC/RMI protocol (Remote Procedure Call / Remote
Method Invocation).  If you have control of both ends of the wire, and
are thus not constrained to use some other protocol like
HTTP/XMLRPC/CORBA/etc, you might consider using Foolscap.

%prep
%setup -qn %{module}-%{version}

%build
find . -name "*.py" -exec 2to3 -w {} \;
%py_build

%install
%py_install

%files
%doc LICENSE doc
%{_bindir}/*
%{python_sitelib}/%{module}*
