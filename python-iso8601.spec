#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	iso8601
Summary:	Simple module to parse ISO 8601 dates
Name:		python-%{module}
Version:	0.1.8
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://pypi.python.org/packages/source/i/iso8601/%{module}-%{version}.tar.gz
# Source0-md5:	b207ad4f2df92810533ce6145ab9c3e7
URL:		https://bitbucket.org/micktwomey/pyiso8601
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses the most common forms of ISO 8601 date strings
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

%prep
%setup -qn %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/iso8601/test_*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/iso8601
%{py_sitescriptdir}/iso8601-%{version}-py*.egg-info
