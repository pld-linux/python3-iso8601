#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (not included in sdist)
%bcond_without	tests	# unit tests

%define 	module	iso8601
Summary:	Simple module to parse ISO 8601 dates
Summary(pl.UTF-8):	Prosty moduł do analizy dat ISO 8601
Name:		python3-%{module}
Version:	2.1.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/iso8601/
Source0:	https://files.pythonhosted.org/packages/source/i/iso8601/%{module}-%{version}.tar.gz
# Source0-md5:	6e33910eba87066b3be7fcf3d59d16b5
URL:		https://bitbucket.org/micktwomey/pyiso8601
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:3.6.2
BuildRequires:	python3-installer
BuildRequires:	python3-poetry-core
%if %{with tests}
BuildRequires:	python3-pytest >= 6.2.2
BuildRequires:	python3-pytz
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3 >= 1.2.1
%endif
Requires:	python3-modules >= 1:3.6.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses the most common forms of ISO 8601 date strings
(e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

%description -l pl.UTF-8
Ten moduł analizuje najbardziej popularne postaci łańcuchów dat ISO
8601 (np. 2007-01-14T20:34:22+00:00) i przekształca na obiekty
datetime.

%package apidocs
Summary:	API documentation for Python iso8601 module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona iso8601
Group:		Documentation

%description apidocs
API documentation for Python iso8601 module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona iso8601.

%prep
%setup -qn %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m zipfile -e build-3/*.whl build-3-test
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest -o pythonpath="$PWD/build-3-test" iso8601/test_iso8601.py
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/iso8601/test_*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/iso8601
%{py3_sitescriptdir}/iso8601-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
