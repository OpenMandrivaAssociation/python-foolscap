%define module	foolscap
%define name	python-%{module}
%define version	0.6.1
%define release	%mkrel 3

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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-2mdv2011.0
+ Revision: 667933
- mass rebuild

* Mon Jan 17 2011 Lev Givon <lev@mandriva.org> 0.6.1-1
+ Revision: 631258
- Update to 0.6.1.

* Tue Dec 28 2010 Lev Givon <lev@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 625612
- Update to 0.6.0.

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.5.1-2mdv2011.0
+ Revision: 590139
- rebuild for python 2.7

* Fri Mar 26 2010 Lev Givon <lev@mandriva.org> 0.5.1-1mdv2010.1
+ Revision: 527759
- Update to 0.5.1.

* Tue Jan 19 2010 Lev Givon <lev@mandriva.org> 0.5.0-1mdv2010.1
+ Revision: 493666
- Update to 0.5.0.

* Wed Jul 22 2009 Lev Givon <lev@mandriva.org> 0.4.2-1mdv2010.0
+ Revision: 398669
- Update to 0.4.2.

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.3.2-2mdv2009.1
+ Revision: 323708
- rebuild

* Sun Oct 19 2008 Lev Givon <lev@mandriva.org> 0.3.2-1mdv2009.1
+ Revision: 295421
- Update to 0.3.2.

* Mon Aug 18 2008 Lev Givon <lev@mandriva.org> 0.3.0-1mdv2009.0
+ Revision: 273137
- import python-foolscap


