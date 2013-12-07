%define module	foolscap

Summary:	Rewrite of Perspective Broker
Name:		python-%{module}
Version:	0.6.4
Release:	5
License:	MIT
Group:		Development/Python
Url:		http://foolscap.lothar.com/
Source0:	http://foolscap.lothar.com/releases/foolscap-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
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
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%files -f FILELIST
%doc ChangeLog LICENSE NEWS README doc

