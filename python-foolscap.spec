%define module	foolscap

Summary:	Rewrite of Perspective Broker
Name:		python-%{module}
Version:	0.13.1
Release:	2
License:	MIT
Group:		Development/Python
Url:		http://foolscap.lothar.com/
Source0:	https://files.pythonhosted.org/packages/b5/af/955c37e197df562b92a049d11a0f5cbae8ab8996007b3a65a88a920b75b0/foolscap-0.13.1.tar.gz
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
%doc LICENSE NEWS README doc
%{_bindir}/*
%{python_sitelib}/%{module}*
