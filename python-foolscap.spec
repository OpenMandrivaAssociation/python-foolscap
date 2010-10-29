%define module	foolscap
%define name	python-%{module}
%define version	0.5.1
%define release	%mkrel 2

Summary:	Rewrite of Perspective Broker
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://foolscap.lothar.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python >= 2.4
Requires:	python-twisted >= 2.4.0
Requires:	python-OpenSSL >= 0.6
BuildRequires:	python-devel >= 2.4
BuildArch:	noarch

%description
Foolscap is a ground-up rewrite of Perspective Broker, which itself is
Twisted's native RPC/RMI protocol (Remote Procedure Call / Remote
Method Invocation).  If you have control of both ends of the wire, and
are thus not constrained to use some other protocol like
HTTP/XMLRPC/CORBA/etc, you might consider using Foolscap.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc ChangeLog LICENSE NEWS README doc
