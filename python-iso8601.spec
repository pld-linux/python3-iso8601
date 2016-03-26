#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	iso8601
Summary:	Simple module to parse ISO 8601 dates
Summary(pl.UTF-8):	Prosty moduł do analizy dat ISO 8601
Name:		python-%{module}
Version:	0.1.11
Release:	1
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/iso8601/
Source0:	https://pypi.python.org/packages/source/i/iso8601/%{module}-%{version}.tar.gz
# Source0-md5:	b06d11cd14a64096f907086044f0fe38
URL:		https://bitbucket.org/micktwomey/pyiso8601
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses the most common forms of ISO 8601 date strings
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

%description -l pl.UTF-8
Ten moduł analizuje najbardziej popularne postaci łańcuchów dat ISO
8601 (np. 2007-01-14T20:34:22+00:00) i przekształca na obiekty
datetime.

%package -n python3-%{module}
Summary:	Simple module to parse ISO 8601 dates
Summary(pl.UTF-8):	Prosty moduł do analizy dat ISO 8601
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
This module parses the most common forms of ISO 8601 date strings
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

%description -n python3-%{module} -l pl.UTF-8
Ten moduł analizuje najbardziej popularne postaci łańcuchów dat ISO
8601 (np. 2007-01-14T20:34:22+00:00) i przekształca na obiekty
datetime.

%prep
%setup -qn %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/iso8601/test_*
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/iso8601/test_*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/iso8601
%{py_sitescriptdir}/iso8601-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/iso8601
%{py3_sitescriptdir}/iso8601-%{version}-py*.egg-info
%endif
